import re

def emailIDValidator(username):
    regexPattern = '^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regexPattern,username):
        return True
    else:
        return False