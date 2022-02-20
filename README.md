
# Registration and Login System Using Python

### Languages Used: 
Python
### Techniques used: 
File Handling, Regex, and Dataframe operations
### Files:
1) **database** - This folder contains `db.csv` file which acts a dummy database and used to store user email Id and password.
2) **emailvalidation.py** - Python module used to check if a user email satisfies all required conditions.
3) **passwordvalidator.py** - Python module used to validate user defined password with pre-defined requirements for a valid password.
4) **login.py** - Python module with all user login related functionalities.
5) **forgotpassword.py** - module to retrive forgotton password
6) **registration.py** - module to create new account with email ID and password
7) **main.py** - main module that combines all other modules mentioned above.

### How to Run:
```
# For Linux
python3 run main.py

# For Windows
python main.py
```
Running main.py file consists of following functionalities in order,

1) User Login : User is required to enter his email Id and password. If successful the program will stop, else User will be asked to enter into Forget password or Registration page.
2) Forget Password : User if not sure about password or forgot, user can retrieve it from db.csv using his registered email id.
3) Registration: If you are a new user, then user can create a new account by entering credentials like email ID and Password.

### Gallery:

#### User Forgot Password and Login
<br>

![forgotPassword](https://user-images.githubusercontent.com/49028941/154853127-6de9a32d-30ef-4b35-ace5-f5cadaa267f1.jpg)

#### User Registration 
<br>

![registration](https://user-images.githubusercontent.com/49028941/154853132-7d9e293c-abf0-47a2-87f0-cd7b09cae55a.jpg)
