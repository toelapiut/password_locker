#!/usr/bin/env python3.6
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
 #=======================================================================================


#function that take three arguments  from class Credential
def creat_user_account(fname,lname,password):

	new_user_account=Credential(fname,lname,password)

	new_user_account.save_credential()
#---------------------------------------------------------

#funtion for saving accounts
def creat_accounts(aname,emails,pword):
	new_account=Account(aname,emails,pword)

	new_account.save_account()

#---------------------------------------------------------

#function to find a user account 
def find_account(passwrd):
	return Credential.find_account(passwrd)

#---------------------------------------------------------

#function to check if the account exists 
def account exists(last_name):
	return Credential.account_exist(last_name)

#---------------------------------------------------------
