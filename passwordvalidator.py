import re

def upperlowercaseChecker(password):
    lowercase = False;uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
            break
    for i in password:
        if i.islower():
            lowercase = True
            break
    return lowercase,uppercase

def specialcharChecker(password):
    var = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if var.search(password) == None:
        return False
    else:
        return True

def digitChecker(password):
    val = any(map(str.isdigit,password))
    return val

def passwordLengthValidator(username,min_len,max_len):
    pwdStatus = False
    if len(username) > min_len and len(username) < max_len:
        pwdStatus = True
    return pwdStatus

def passwordValidation(password):
    check0 = passwordLengthValidator(password,5,16)
    check1,check2 = upperlowercaseChecker(password)
    check3 = digitChecker(password)
    check4 = specialcharChecker(password)
    if ((check0 and check1 and check2 and check3 and check4) == True):
        return True
    else:
        return False