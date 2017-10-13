import unittest#importing unittest
from locker import Credential #importing Credentials

#creating a unittest 
class Test(unittest.TestCase):

#creating a set up test 
	def setUp(self):

		self.new_credential=Credential("apiut","toel","toelapiut7@gmail.com","Hello, This are my notes and hope they work")

#creation of an initializing test 
	def test_init(self):
		self.assertEqual(self.new_credential.first_name,"apiut")
		self.assertEqual(self.new_credential.last_name,"toel")
		self.assertEqual(self.new_credential.email,"toelapiut7@gmail.com")
		self.assertEqual(self.new_credential.note,"Hello, This are my notes and hope they work")

#testing if my credentials are being saved
	def test_save_credential(self):
		self.new_credential.save_credential()

		self.assertEqual(len(Credential.login_credentials),1)

#tearing Down function to clear class variable
	def tearDown(self):
		login_credentials=[]

#saving multiple credentials 
	def save_multiple_credentials(self):

		self.new_credential.save_credential()

		another_credential=Credential("apiut","toel","toelapiut7@gmail.com","Hello, This are my notes and hope they work")
		another_credential.save_credential()
		self.assertEqual(len(Credential.login_credentials),1)


if __name__=="__main__":
	unittest.main(verbosity=2) 