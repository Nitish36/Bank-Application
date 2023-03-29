import mysql.connector
import random
from colorama import Fore

def display():
    print("----- User Deatils -----")
    mycursor.execute("SELECT * FROM bank")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def insertion():
    pinC = random.randrange(1000,9999)      # pin and cvv is randomly generated for each user
    cvvC = random.randrange(100,999)
    pinD = random.randrange(1000,9999)      # pin and cvv is randomly generated for each user
    cvvD = random.randrange(100,999)
    
    print("Enter a valid username")
    username = input()
    print("Enter a valid address")
    address = input()
    print("Enter valid aadhar number")
    adhar = input()
    print("Enter phone number")
    phone = (input())
    if(len(phone) > 10):
        print("Invalid phone number")
    
    print("Enter a balance amount") 
    balance = int(input())
	
    
    mycursor.execute("""
                 INSERT INTO bank(username,address,adhar,mobile,pinC,cvvC,pinD,cvvD,balance)
                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                 """,(username,address,adhar,phone,pinC,cvvC,pinD,cvvD,balance))
    print("Data Entered Successfully")

def deletion(username):
    sql_delete_query = '''
        Delete from bank WHERE username = %s
    '''
    print("Confirm username deletion by entering the same username again")
    deleted_username = (input(),username)
    mycursor.execute(sql_delete_query,deleted_username)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    

def update(ch,username,balance):
    
    if ch == 1:
        sql_update_query = """
			Update bank set address = %s WHERE username = %s
        """
        print("Enter the new address")
        new_address = (input(),username)
        mycursor.execute(sql_update_query,new_address)
        mydb.commit()
    
    elif ch == 2:
        sql_update_query = """
			Update bank set adhar = %s WHERE username = %s
        """
        print("Enter the new adhar")
        new_adhar = (input(),username)
        mycursor.execute(sql_update_query,new_adhar)
        mydb.commit()
        
    elif ch == 3:
        sql_update_query = """
			Update bank set mobile = %s WHERE username = %s
        """
        print("Enter new 10 digit phone number:")
        new_phone = (input(),username)
        if(len(new_phone) > 10):
            print("Invalid phone number")
            
        mycursor.execute(sql_update_query,new_phone)
        mydb.commit()
    
    elif ch == 4:
        print("Press + to deposit")
        print("Press - to withdrw")
        che = input()
        if che == '+':
            print("Enter a valid amount")
            amount = int(input())
            if(amount<0):
                print("Amount cannot be negative")
            else:
                balance = balance+amount
                mycursor.execute(balance,balance)
                mydb.commit()
        
        if che == '-':
            print("Enter the amount you want to withdraw")
            amount = int(input())
            if amount>balance:
                print("Insufficient balance")
            else:
                balance = balance-amount
                mycursor.execute(balance,balance)
                mydb.commit()

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = ""
	)
 
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE Banker")
#mycursor.execute("SHOW DATABASES")
mycursor.execute("USE Banker")
#mycursor.execute("CREATE TABLE bank (username VARCHAR(20),address VARCHAR(20), adhar INT,mobile VARCHAR(20),pinC INT,cvvC INT,pinD INT,cvvD INT)")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("ALTER TABLE bank MODIFY COLUMN username VARCHAR(20) PRIMARY KEY")
#mycursor.execute("ALTER TABLE bank ADD COLUMN Balance INT")

#-------------Main Program---------------#

#-------CREATING USER ACCOUNT-------#
print("---------- Banking Application ----------")
print("---------- Registration Form ----------")
choice = 0
balance = 0
print("Select 1 to Register")         # This step is insertion
print("Select 2 for updation") 		  # This step is an updation
print("Select 3 for display of informaton")		#Display
print("Select 4 to close the account")    #Deletion


while(True):
    print("Enter a choice")
    choice = int(input())    
    if(choice == 1):
        insertion()
        mydb.commit()
        
    elif(choice == 2):
        print("Updation of info")
        print("Select any of the choices to update ur info and enter the ur username also ")
        print("Enter 1 to update address")
        print("Enter 2 to update adhar")
        print("Enter 3 to update phone number")
        print("Enter 4 to update ur balance amount")
        ch = 0
        print("Enter ur choice")
        ch = int(input())
        print("Enter ur username")
        username = input()
        update(ch,username,balance)

    elif(choice == 3):
         display()
    
    elif(choice == 4):
        print("Deletion of record")
        print("Enter the username to be deleted")
        username = input()
        deletion(username)
    
    else:
        exit(0)


