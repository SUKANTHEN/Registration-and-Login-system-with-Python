from passwordvalidator import passwordValidation
from forgotpassword import forgotPassword
from emailvalidation import emailIDValidator
from registration import registration
from login import loginScript

def registrationLoop():
    val = registration()
    if val==True:
        print("Registered Sucessfully")
    elif val == "Weak Credentials":
        print("Set Strong User Credentials")
    elif val == "Email ID Exists already":
        print("Email ID Already exists.")
 
logs = loginScript()
if logs == 1:
    print("Log in Successfull")
else:
    print("Log in Failed.")
    val = int(input("Press --> 1 for Forgot Password, and 2 for Registration :"))
    if val == 1:
        logs,status = forgotPassword()
        if status == 1:
            print(f"Retrived Password : {logs}")
            logs = loginScript()
            if logs == 1:
                print("Log in Successfull")
            else:
                print("Log in Failed.")
        else:
            print(logs)
            val = registrationLoop()

    elif val == 2:
        val = registrationLoop()
    else:
        print("Kindly Enter 1 or 2.")