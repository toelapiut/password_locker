from account import Account
import random

main_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","!","@","#","$","%","^","&","*","(",")","_","-","+","?","/"]
#class blue print
class Credential:

	login_credentials=[]

	def __init__(self,first_name,last_name,password,email):

		self.first_name=first_name
		self.last_name=last_name
		self.password=password
		self.email=email

 

   
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
		print(x)
	generate_password()
			

#Methods to describe the functionality 

# save credential function
	def save_credential(self):

		Credential.login_credentials.append(self)

#delete account function
	def delete_credential(self):
		Credential.login_credentials.remove(self)


#Decorator
#find account function

	@classmethod
	def find_account(cls,passwrd):

		for passed in cls.login_credentials:
			if passed.password == passwrd:
				return passed





	@classmethod
	def account_exist(cls,email):
		for femail in cls.login_credentials:
			if femail.email==email:
				return True
		return False