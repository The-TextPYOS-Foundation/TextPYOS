#This is an exact recreation of the 2023 version of TextPYOS (At the time called "Python.OS")
#Gramatical errors & bugs included (It's a 1:1 of the OG code, no changes made outside of comments.)

import time
Name = input("Hello, user, What would you like to be know as? :")
Password = input("Hello, " + Name + " What would you like your password to be? :")
print ("Your name is, " + Name + " And your password is " + Password)
print ("Starting up...")
time.sleep(2.5)
CorrectName = input ("Please input your name: ")
if CorrectName == Name:
    input ("Please input your password :")
else:
    print ("Incorrect")
print ("Checking...")
time.sleep(2)
print ("Authenticating...")
time.sleep(2)
print ("Complete...")
time.sleep(0.5)
print ("Welcome, " + Name + " We are glad to see you.")
time.sleep(1)
Usedbefore = input("have you used this software before? :")
if Usedbefore == "Yes" or "yes":
    print ("Oh, Okay then! Please keep in mind that this is in early development and may have bugs!")
else:
    print ("Oh, Good! Well, it's simple. You just say one of the keywords and something will happen!")

    print ("The keywords are: Books, Games, And Other. Say one and see what you can do!")
Books = ["Art of the panda", "Coding For Dummies", "How to brickblockstudio book.1",]
Games = ["Brickblockstudio", "Pthon", "Brickblock",]
Other = ["Settings", "Files", "NotASecret.exe"]
Userinput = input
if Userinput == "Books" or "books":
    print ("test")
else:
    print ("error")

#Alright--2025 me is back.
#This code is absolutley abhorrent.
#Anyways, have fun (If you can even do that with this).