
#Created by Talha Rana student of UET KSK Lahore

"""This is basically a number guessing game. To start this make a login.txt file and run the code 
then you have to select the range"""







import random
import os
import time
def range_menu():
    while True:
        print("Play game with ranges:")
        print("1. 1->5")
        print("2. 1->50")
        print("3. 1->100")
        print("4. 1->1000")
        choice=int(input("Enter the number of range of your choice:")) #user enter the range on which he wants to play
        if(choice<=4 and choice>=1):
            time.sleep(1)
            os.system("cls") #clear the terminal o run time
            return choice # return the choice of the user if the choice is valid means it is in the range of 1->4
        else:
            print("Invlaid input")
def header(): # for the header only
        print("\n\n\n\n\n\n\n\n\n\n\n")
        print( "\t\t        <><><>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>--<><><>") 
        print("\t\t        <><><>---<>---<>---<>---<>---<>---<< HIDDEN DIGIT HUNT  >>---<>---<>---<>---<>---<>---<>---<><><>")
        print( "\t\t        <><><>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>--<><><>")
        print("\n")
def menu(): #for the selection that they have an account or not
    header()
    num=(input("1.Login for account (L)\n2.Create new account(C)")).upper()
    return num
def account_creation():
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    with open("login.txt", "a") as f:
        f.write(f"\n{new_username},{new_password}") #adding new data into hte file
    
    print("Account created successfully!")
def login(): 
        count=0
        with open("login.txt","r") as f: 
            data=f.read() #reading data from the file
            pass_pair=data.split("\n") # In the file username,password store in this manner it will take a record(line) wise   data in pass_pair
            while True:
                if(count!=0):
                    os.system("cls")
                    header()
                    choice=input("For try again(C) or Exit(E):").upper()
                    if(choice=="E"):
                        return False

            
                username=input("Enter the username:")
                password=input("Enter teh pass word:")

                for val in pass_pair:
                    count+=1       
                    if(val.strip()): #skip empty line
                        stored_username , stored_password=val.split(",") #separate username and password in two different varibale
                    if username==stored_username and password==stored_password:
                        print("Login is successfull")
                        time.sleep(0.9) #to delay something for this you have to import time module
                        os.system("cls")  #to clear the terminal at runtime
                        return True
print("Invalid id or password")

def main(): # controls the login and creation of new account
    while True:
        choice=menu()
       
        if choice == 'L':
            login()
            return True
        elif choice == 'C':
            account_creation()
        else:
            print("Invalid choice. Please enter 'L' to login or 'C' to create a new account.")
            
# main function starts
header()
main()
header()
range=range_menu() #choice store in this
header()
print("\t\t\t\t\t The is started with range",end=" ")
if(range==1): # these if and elif can set the range of the game
    print(" is 1->5")
    randomnum=random.randint(1,5)   #randint is the function int he random module where the parenthesis we have to give the limit. In this case the limit is 1 ->5
elif(range==2):
        print(" is 1->50")
        randomnum=random.randint(1,50)
elif(range==3):
        print(" is 1->100")
        randomnum=random.randint(1,100)
else:
        print(" is 1->1000")
        randomnum=random.randint(1,1000)
print("GUESS THE NUMBER IN 10 ATTEMPT")
i=0
while i<10 : # these while loop is the very important body of the code
    usernum=(input("Guess the target or Exist(E):")).upper()
    if(usernum=="E"):
        print("\t\t        <><><>---<>---<>---<>---<>---<>---<< YOU QUIT THIS IS GAME. YOU DIDNOT FIND THE NUMBER  >>---<>---<>---<>---<>---<>---<><><>")
        print("The number was ",randomnum)
        break
    usernum=int(usernum)
    if(usernum==randomnum):
        print("\t        <><><>---<>---<>---<>---<>---<>---<< CONGRATUALTION YOU HAVE SUCCESSFULLY GUESS THE RIGHT NUMBER  >>---<>---<>---<>---<>---<>---<><><>")
        break
    elif(usernum>randomnum):
        print("Your guess is too big.Take a smaller guess.")
        
    else:
        print("Your guess is too small.Take a bigger guess.")
    i+=1
    print("\t\tYour total number of attempt left is",10-i)
if(i==9):
     print("All your attempts are over.")
     print("The number is ",randomnum)
print("\t\t        <><><>---<>---<>---<>---<>---<>---<< GAME OVER  >>---<>---<>---<>---<>---<>---<><><>")
