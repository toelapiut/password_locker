#!/usr/bin/env python3.6
from locker import Credential,Account
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
def save_accountsx(creden):
	creden.save_credential()


#---------------------------------------------------------

#function to find a user account 
def find_account(passwrd):
	return Credential.find_account(psword)

#---------------------------------------------------------

#function to check if the account exists 
def account_existx(passwrd):
	return Credential.account_exist(passwrd)

#---------------------------------------------------------

#=========================================================
				#Account functions 
#=========================================================

from locker import Account

#function to delete unwanted account
def delete_accounts(account):
	accounts.delete_account()

#---------------------------------------------------------

#funtion for create accounts
def create_account1(aname,emails,pword):
	new_account=Account(aname,emails,pword)
	return new_account

#---------------------------------------------------------

#function save account 
def save_user_account(ac):
	ac.save_account_user()

#---------------------------------------------------------

#function to find accounts
def find_existing_account(passwrd):
	return Account.find_accounts(passwrd)

#--------------------------------------------------------

#function to find existing accounts
def account_existed(emails):
	return Account.account_exists(emails)

#---------------------------------------------------------

#Function to display all your accounts
def display_account():
	return Account.display_accounts()

#---------------------------------------------------------

#function to generate a new password
def random_password():
	return Account.generate_password()



#=========================================================
					#End of functions
#=========================================================

#---------------------------------------------------------

#=========================================================
					#App creation
#=========================================================

print('\n')
#--------------------------------------------------------

#collection of user info
global saved_user;

def creating_account():
	print("Hey! Hello! It's nice to have you around! You're about to change your life.")

	print("\n")

	print("New User")
	print("-"*22)
	

	print("Enter You first name!")
	fname=input().lower().capitalize().strip()
	print("-"*22)

	print("Enter last name!")
	lname=input().lower().capitalize().strip()
	print("-"*22)

	print("Key In your password")
	psword=input().strip()
	print("-"*22)


	saved_user=save_accountsx(creat_user_account(fname,lname,psword))
	print("\n")
	print(f"Thank you!! {fname}-{lname} You've been added to our list ")

creating_account()

#--------------------------------------------------------


def main():
#confirmation of user credentials
	# while True:
	print("Hello,LogIn!")

	
	print("Enter Password")

	# while True:

	user_password=input().strip()
	print("-"*22)


	if account_existx(user_password):
		while True:
			print("Well, Use the following codes : ca - create a new account, da - display contacts, fa -find a account, ex -exit the contact list, del-del account")

			print("Enter code")
			usercode= input().strip().lower()

			if usercode=='ca':

				print("Enter Account Name")
				aname=input()
				print("\n")
				
				print("Enter email")
				print("-"*22)
				emails=input()
				print("\n")

				print("Do you want to create your own password?Y/N")

				choice=input().strip().lower()

#generation of password
				if choice=="n":
					pword=random_password()
					print(random_password())

				elif choice=="y":
					print("Enter Password")
					print("-"*22)
					pword=input()
				save_user_account(create_account1(aname,emails,pword))


			elif usercode=="da":
				if display_account():

					for accs in display_account():
						print(f" Account Name:{accs.account_name} \n Email: {accs.emails} \n password: {accs.passwords} \n ======================")

			elif usercode=="del":
				
			elif usercode=="ex":
				print("Bye....Come Again!")
				break
			else:
				print('fuck u')
			


	else:
		print()



if __name__=='__main__':
	main()
