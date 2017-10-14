#!/usr/bin/env python3.6
from locker import Credential
from locker import Account
import random

def function():
	print(" __      __   _________    __           __            __________    ")
	print("|  |    |  | |         |  |  |         |  |          /           \ ")
	print("|  |    |  | |    -----   |  |         |  |         |   _______   | ")
	print("|  |    |  | |   |        |  |         |  |         |  /       \  | ")
	print("|  |    |  | |   |        |  |         |  |         |  |       |  | ")
	print("|   ----   | |    ------  |  |         |  |         |  |       |  | ")
	print("|          | |          | |  |         |  |         |  |       |  | ")
	print("|   ____   | |    ------  |  |         |  |         |  |       |  | ")
	print("|  |    |  | |   |        |  |         |  |         |  |       |  | ")
	print("|  |    |  | |   |        |  |         |  |         |  |       |  | ")
	print("|  |    |  | |    ______  |   -------  |   -------  |  \_______/  | ")
	print("|  |    |  | |          | |          | |          | \             / ")
	print(" --      --   ----------   ----------   ----------    -----------  ")
	
function()
    #END OF HELLO ANIMATION 
 #========================================================

#=========================================================
				#Credential functions 
#=========================================================

#function that take three arguments  from class Credential
def creat_user_account(fname,lname,psword):

	new_user_account=Credential(fname,lname,psword)
	return new_user_account

#---------------------------------------------------------

#function to save accounts
def save_account(account):
	account.save_credential()

#---------------------------------------------------------

#funtion for saving accounts
def save_accounts(aname,emails,pword):
	new_account=Account(aname,emails,pword)

	new_account.save_account()

#---------------------------------------------------------

#function to find a user account 
def find_account(passwrd):
	return Credential.find_account(passwrd)

#---------------------------------------------------------

#function to check if the account exists 
def account_exists(last_name):
	return Credential.account_exist(last_name)

#---------------------------------------------------------

#=========================================================
				#Account functions 
#=========================================================

#function to delete unwanted account
def delete_accounts(account):
	accounts.delete_account()


#---------------------------------------------------------

#function to find accounts
def find_existing_account(passwrd):
	return Account.find_accounts(passwrd)

#--------------------------------------------------------

#function to find existing accounts
def account_exists(emails):
	return Account.account_exists(emails)

#---------------------------------------------------------

def display_account():
	return Account.display_accounts()


#=========================================================
					#End of functions
#=========================================================

#---------------------------------------------------------

#=========================================================
					#App creation
#=========================================================

print('\n')

global saved_user;

def creating_account():
	print("Hey! Hello! It's nice to have you around! You're about to change your life.")

	print("\n")

	print("New User")
	print("-"*22)
	

	print("Enter You first name!")
	fname=input()
	print("-"*22)

	print("Enter last name!")
	lname=input()
	print("-"*22)

	print("Key In your password")
	psword=input()
	print("-"*22)


	saved_user=save_account(creat_user_account(fname,lname,psword))
	print("\n")
	print(f"Thank you!! {fname}-{lname} You've been added to our list ")

creating_account()

def main():

	print("Key In your password")




if __name__=='__main__':
	main()
