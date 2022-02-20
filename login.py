import pandas as pd

dataFilePath = "database/db.csv"
data = pd.read_csv(dataFilePath)

def userIDAuthentication(emailID,password):
    id = False
    pwd = False
    if emailID in data["username"].values:
        id = True
    if password in data["password"].values:
        pwd = True
    if id == pwd == True:
        return 1
    elif (id == False):
        return 0
    else:
        return 0

def loginScript():
    print("#---------------- Login Page ----------------#")
    userid = input("Enter your Email ID :")
    password = input("Enter your Password :")
    logs = userIDAuthentication(userid,password)
    return logs