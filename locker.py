import random

main_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","!","@","#","$","%","^","&","*","(",")","_","-","+","?","/"]
#class blue print

global login_credentials
global accounts_list


class Credential:

	login_credentials=[]

	def __init__(self,first_name,last_name,password):

		self.first_name=first_name
		self.last_name=last_name
		self.password=password
 



#-------------------------------------------------------------#			

#Methods to describe the functionality 

# save credential function
	def save_credential(self):

		Credential.login_credentials.append(self)

#Decorator
#find account function

	@classmethod
	def find_account(cls,passwrd):

		for passed in cls.login_credentials:
			if passed.password == passwrd:
				return passed



	@classmethod
	def account_exist(cls,passwrd):
		for femail in cls.login_credentials:
			if femail.password==passwrd:
				return True
		return False

################################################################
class Account:

	accounts_list=[]

	def __init__(self,account_name,emails,passwords):

		self.account_name=account_name
		self.emails=emails
		self.passwords=passwords


#------------------------------------------------------------------
##password generator
	def generate_password():
		g_password=[]	
		randspasslength=random.randint(10,15)
		count=0
		while count<=randspasslength:
			count+=1
			indexes=[random.randint(0,62)]	
			for x in indexes:
				passx=main_list[x]
			g_password.append(passx)
		g_password.append(passx)
		x=''.join(g_password)
		return x
	generate_password()
#--------------------------------------------------------

#end of password generator	

#-------------------------------------------------------
	def save_account_user(self):

		Account.accounts_list.append(self)
#-------------------------------------------------------
			        #End

#-------------------------------------------------------
#delete account function
	def delete_account(self):
		Account.accounts_list.remove(self)
#-------------------------------------------------------
					#End

				
#Decorator
#-------------------------------------------------------
#find account function

	@classmethod
	def find_accounts(cls,aname):

		for passed in cls.accounts_list:
			if passed.account_name == aname:
				return passed
#-------------------------------------------------------
					#End

#decorators
#-------------------------------------------------------
#check for existance
	@classmethod
	def account_exists(cls,aname):
		for femail in cls.accounts_list:
			if femail.account_name==aname:
				return True
		return False
#------------------------------------------------------
				#End

#------------------------------------------------------

#
	@classmethod
	def display_accounts(cls):
		return cls.accounts_list
