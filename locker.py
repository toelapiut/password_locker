class Credential:

	login_credentials=[]

	def __init__(self,first_name,password,last_name,email,note):

		self.first_name=first_name
		self.last_name=last_name
		self.password=password
		self.email=email
		self.note=note


#Methods to describe the functionality 

# save credential function
	def save_credential(self):

		Credential.login_credentials.append(self)

	def delete_credential(self):
		Credential.login_credentials.remove(self)