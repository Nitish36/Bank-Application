import random

def display(finalDirectory):
    print("----- User Deatils -----")
    print(finalDirectory)
    
print("---------- Banking Application ----------")
choice = 0
print("Select 1 to enter username")         # username
print("Select 2 to enter address")          # address
print("Select 3 to enter adhar")            # adhar
print("Select 4 to enter phone")            # phone
print("Select 5 to display info")           # display info

myDict = {}
finalDirectory = {}
while(True):
    print("Enter a choice")
    choice = int(input())
    
    pinC = random.randrange(1000,9999)      # pin and cvv is randomly generated for each user
    cvvC = random.randrange(100,999)
    pinD = random.randrange(1000,9999)      # pin and cvv is randomly generated for each user
    cvvD = random.randrange(100,999)
    
    
    if(choice == 1):
        print("Enter a valid username")
        username = input()
        myDict["username"] = username
    elif(choice == 2):
        print("Enter a valid address")
        address = input()
        myDict["address"] = address
    elif(choice == 3):
        print("Enter valid aadhar number")
        adhar = input()
        myDict["adhar"] = adhar
    elif(choice == 4):
        print("Enter phone number")
        phone = (input())
        if(len(phone) > 10):
            print("Invalid phone number")
        myDict["phone"] = phone
    elif(choice == 5):
        myDict["pinC"] = pinC
        myDict["cvvC"] = cvvC
        myDict["pinD"] = pinD
        myDict["cvvD"] = cvvD
        finalDirectory.update(myDict)
        display(finalDirectory)
    
    else:
        exit(0)
