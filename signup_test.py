import unittest#importing unittest
from locker import Credential #importing Credentials

#creating a unittest 
class Test(unittest.TestCase):

#creating a set up test 
	def setUp(self):

		self.new_credential=Credential("apiut","toel","QwertY")

#creation of an initializing test 
	def test_init(self):
		self.assertEqual(self.new_credential.first_name,"apiut")
		self.assertEqual(self.new_credential.last_name,"toel")
		self.assertEqual(self.new_credential.password,"QwertY")
		

#testing if my credentials are being saved
	def test_save_credential(self):
		self.new_credential.save_credential()

		self.assertEqual(len(Credential.login_credentials),1)

#tearing Down function to clear class variable
	def tearDown(self):
		Credential.login_credentials=[]

#saving multiple credentials 
	def test_save_multiple_credentials(self):

		self.new_credential.save_credential()

		another_credential=Credential("James","Gitau","QWERTY")
		another_credential.save_credential()

		self.assertEqual(len(Credential.login_credentials),2)


#access the account by password
	def find_account_by_password(self):
		self.new_credential.save_credential()

		another_credential=Credential("James","Gitau","QWERTY")
		another_credential.save_credential()

		account_found=Credential.find_account("QWERTY")

		self.assertEqual(account_found.last_name,another_credential.last_name)

#account exists function
	def test_account_exists(self):

		self.new_credential.save_credential()
		another_credential=Credential("James","Gitau","QWERTY")
		
		another_credential.save_credential()

		exist_account=Credential.account_exist("QWERTY")

		self.assertTrue(exist_account)

#====================================================================================
from locker import Account
class Tested(unittest.TestCase):

	def setUp(self):

		self.new_acc=Account("FaceBook","toelapiut7@gmail.com","QwertY")

	#creation of an initializing test 
	def test_init(self):
		self.assertEqual(self.new_acc.account_name,"FaceBook")
		self.assertEqual(self.new_acc.emails,"toelapiut7@gmail.com")
		self.assertEqual(self.new_acc.passwords,"QwertY")
		


#testing if my credentials are being saved
	def test_save_account(self):
		self.new_acc.save_account()

		self.assertEqual(len(Account.accounts_list),1)

#tearing Down function to clear class variable
	def tearDown(self):
		Account.accounts_list=[]

#saving multiple credentials 
	def test_save_multiple_account(self):

		self.new_acc.save_account()

		another_account=Account("Twitter","toelapiut7@gmail.com","QWERTY")
		another_account.save_account()

		self.assertEqual(len(Account.accounts_list),2)

#delete account if someone doesn't need the account 
	def test_delete_account(self):

		self.new_acc.save_account()

		another_account=Account("Twitter","toelapiut7@gmail.com","QWERTY")
		another_account.save_account()

		self.new_acc.delete_account()

		self.assertEqual(len(Account.accounts_list),1)

#access the account by password
	def test_find_account_by_password(self):
		self.new_acc.save_account()

		another_account=Account("Twitter","toelapiut7@gmail.com","QWERTY")
		another_account.save_account()

		account_found=Account.find_accounts("QWERTY")

		self.assertEqual(account_found.emails,another_account.emails)

#account exists function
	def test_account_exists(self):

		self.new_acc.save_account()

		another_account=Account("Twitter","toelapiut7@gmail.com","QWERTY")
		another_account.save_account()

		exist_account=Account.account_exists("toelapiut7@gmail.com")

		self.assertTrue(exist_account)


if __name__=="__main__":
	unittest.main(verbosity=2) 