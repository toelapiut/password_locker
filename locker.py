class Credential:

	login_credentials=[]

	def __init__(self,first_name,last_name,password,email,note):

		self.first_name=first_name
		self.last_name=last_name
		self.password=password
		self.email=email
		self.note=note


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