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
def find_existing_account(a_name):
	return Account.find_accounts(a_name)

#----------------------------------------------------------

#function to delete unwanted account
def delete_accounts(account):
	account.delete_account()

#--------------------------------------------------------

#function to find existing accounts
def account_existed(a_name):
	return Account.account_exists(a_name)

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
def main():
	

	print("Hey! Hello! It's nice to have you around! You're about to change your life.")
	
	


	while True:
		print("Use the following codes : UA- create a new user Account, LN - Log In,EXIT -exit completely")
		print("Enter a code")
		shortcode=input().lower().strip()
		print("\n")
		print("\n")
		if shortcode=="ua":
			
			# print("Use the following codes : UA- create a new user Account, LN - Log In,EXIT -exit completely")
			print("#"*22)
			print("\n")

			print("New User")
			print("-"*22)
			

			print("Enter Your first name!")
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

		
		elif shortcode=="ln":
#--------------------------------------------------------

	#confirmation of user credentials
		
			print("Hello,LogIn!")

			
			print("Enter Password")		

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
		#----------------------------------------------------------------------

		#displaying all the users information
					elif usercode=="da":
						if display_account():

							for accs in display_account():
								print(f" Account Name:{accs.account_name} \n Email: {accs.emails} \n password: {accs.passwords} \n ======================")
						else:
							print("No search Account ..Try again.")
		#----------------------------------------------------------------------

		#deleting a specific contact
					elif usercode=="del":
						print("-"*10)
						print("Enter -Account Name- to delete")
						user_acc_name=input()
						print("\n")

						if  account_existed(user_acc_name): 
							search_account=find_existing_account(user_acc_name)
							delete_accounts(search_account)
							print("\n")

						else:
							print("Account doesnt exist")
		#----------------------------------------------------------------------


		#find the contact and display it 	
					elif usercode=="fa":
					    print("Enter -Account Name-")
					    user_acc_name=input()
					    print("\n")

					    if  account_existed(user_acc_name): 
						    search_for_account=find_existing_account(user_acc_name)
						    print(f"Account Name:{search_for_account.account_name} \n Email:{search_for_account.emails} \n Password:{search_for_account.passwords} \n =================================================")
							#---------------------------------------------------------------------
		#Exiting from the program				
					elif usercode=="ex":
						print("Bye....Come Again!")
						break	

					else:
						print("Please try again")
						# elif shortcode=="exit":
						# print("See ya'!!")	
		else:
			print("Please create an account with")
			
#-----------------------------------------------------------------------
	

#====================================================================
								#END
#=======================================================================
if __name__=='__main__':
	main()
