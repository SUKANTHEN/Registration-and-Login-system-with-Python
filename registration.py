from passwordvalidator import passwordValidation
from emailvalidation import emailIDValidator
from csv import writer
import pandas as pd

dataFilePath = "database/db.csv"
data = pd.read_csv(dataFilePath)

def register():
    email = input("Enter your email id :")
    password = input("Set your password :")
    return email,password

def registration():
    val = False; dataList = []
    print("#---------------- Registration Page ----------------#")
    email,password = register()
    emailCheck = emailIDValidator(email)
    passwordCheck = passwordValidation(password)
    if (emailCheck and passwordCheck) == True:
        dataList.append(email)
        dataList.append(password)
    else:
        return "Weak Credentials"
    if email not in data["username"].values:
        with open('database/db.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(dataList)
            f_object.close()
            val = True
    else:
        return "Email ID Exists already"
    return val