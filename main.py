import sqlite3
import hashlib
import binascii
import os
conn = sqlite3.connect('database.db')  # Establish Database Connection


def main():
    # create tables
    if conn is not None:
        print("Connection established successfully!")
    else:
        print("Error! Cannot create the database connection.")


def hash_password(password):
    # A password will be hashed in order to be stored in the DB
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_enc_password, userGivenPassword):
    # Verify an ecrypted (already existing in the DB) password against one provided by user
    salt = stored_enc_password[:64]
    stored_enc_password = stored_enc_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  userGivenPassword.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_enc_password


# Function to retrieve the hashed password and compare it
def passComparison(username, password):
    global conn
    query = conn.execute(
        f"select * from player where username='{username}'")
    query_result = query.fetchall()
    passHashDB = ''
    for row in query_result:
        passHashDB = row[2]
    return verify_password(passHashDB, password)


def insertNewData(username: str, password: str, email: str):
    stored_enc_password = hash_password(password)
    #print("Encrypted password: " + stored_enc_password)
    conn.execute(
        f"insert into player (ID, username, password, email) VALUES (NULL, '{username}', '{stored_enc_password}', '{email}')")
    conn.commit()
    print("Records created successfully")
