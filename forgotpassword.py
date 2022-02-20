import pandas as pd

dataFilePath = "database/db.csv"
df = pd.read_csv(dataFilePath)

def passwordRetrieval(emailid):
    status = 0
    if emailid in df["username"].values:
        usernames = df["username"].tolist()
        index = usernames.index(emailid)
        passwords = df["password"].tolist()
        val = passwords[index]
        status = 1
    else:
        val = "Invalid Email ID. Kindly Register your Credentials"
    return val,status

def forgotPassword():
    print("#---------------- Forgot Password Page ----------------#")
    id = input("Enter E-mail ID :")
    logs,status = passwordRetrieval(id)
    return logs,status