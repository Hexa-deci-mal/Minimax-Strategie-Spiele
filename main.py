import sqlite3
import hashlib
import binascii
import os

from numpy import dtype


# Establish Database Connection
conn = sqlite3.connect('database.db')


def main():

    # create tables
    if conn is not None:
        print("Connection established successfully!")

    else:
        print("Error! Cannot create the database connection.")


# def outputDataFromDB():

    cursor = conn.execute("select * from player")
    for row in cursor:
        print("ID = ", row[0])
        print("user_name = ", row[1])
        print("password = ", row[2])
        print("created_date = ", row[3])
        print("updated_date = ", row[4])
        print("email_adress = ", row[5])
        print("rating = ", row[6]), "\n"

    conn.close()


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_enc_password, userGivenPassword):
    """Verify a stored_enc_password password against one provided by user"""
    salt = stored_enc_password[:64]
    stored_enc_password = stored_enc_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  userGivenPassword.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_enc_password


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
    print("Encrypted password: " + stored_enc_password)
    conn.execute(
        f"insert into player (ID, username, password, email) VALUES (NULL, '{username}', '{stored_enc_password}', '{email}')")
    conn.commit()
    print("Records created successfully")
    conn.close()


if __name__ == '__main__':
    main()
    insertNewData()
