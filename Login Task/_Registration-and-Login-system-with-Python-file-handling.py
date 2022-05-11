#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to my portal")
email=str(input("Enter you email id: "))
def validemail(email):
    try:
        if all([('@' in email),(email.index('.')-email.index('@'))>1,(email[0]!='@'),email[0].isalpha()]):
            return True
        else:
            return False
    except:
        pass
def validpassword(password):
    try:
        if all([len(password)in range(8,16),password.isalnum()!=True,password.islower()!=True,password.isupper()!=True]):
            return True
        else:
            return False
    except:
        pass
def login():
    email=str(input("Enter you email id: "))
    db=open("data2.txt",'r')
    x=[]
    for i in db:
        x.append(i)
    x[0].split(",")
    if email in x[0].split(','):
        password=str(input("Enter your password: "))
        a=(x[0].split(',')).index(email)
        if password==(x[0].split(','))[a+1]:
            print("Successfully logged in")
            db.close()
        else:
            print("your password does not match with your email id")
            reset=str(input("Would you like to reset your password: Y/N"))
            if reset.upper()=='Y':
                email=str(input("Enter you email id: "))
                email1=str(input("Please Re-Enter you email id: "))
                db=open("data2.txt",'r')
                x=[]
                for i in db:
                    x.append(i)
                if email in (x[0].split(',')):
                    if email==email1:
                        a=(x[0].split(',')).index(email)
                        print(f"Here is your password: {(x[0].split(','))[a+1]}")
                        db.close()
                        login()
                    else:
                        print("Please update correct email ID's twice")
                        login()
                else:
                    print("Please enter correct email ID")
            else:
                retry=str(input("Would you like to retry again: Y/N "))
                if retry.upper()=='Y':
                    login()
                else:
                    print("Thank you for visiting, get back with right credentials")
    else:
        print("Please enter correct email ID") 
if validemail(email)==True:
    password=str(input("Enter your password: "))
    if validpassword(password)==True:
        db=open("data2.txt",'r')
        x=[]
        for i in db:
            x.append(i)
        if len(x)==0:
            db=open("data2.txt",'a')
            db.write(email+','+password+",")
            print("Successfully registered to system")
            db.close()
            login()
        else:
            db=open("data2.txt",'r')
            x=[]
            for i in db:
                x.append(i)
            x[0].split(",")
            if email in x[0].split(','):
                print("Account already exists, please login")
                db.close()
                login()
            else:
                db=open("data2.txt",'a')
                db.write(email+','+password+",")
                print("Successfully registered to system")
                db.close()
                login()
    else:
        print("Enter valid password satisfying all requirements")
else:
    print("Enter valid email satisfying all requirements")

