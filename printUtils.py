'''
Utilities that provide easy console output options. Intended use is for creating test outputs and for providing easy to use error messages.
'''

# Prints a message to console using red color.
def printErrorMsg(msg):
    print(f'\033[91m{msg}\033[0m')

