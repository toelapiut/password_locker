import unittest
from account import Account


class Tests(unittest.TestCase):

	def setUp(self):

		self.new_account=Account("jamesgitau67@gmail.com","qwertyui")

#creation of an initializing test 
	def test_init(self):
		self.assertEqual(self.new_account.emails,"jamesgitau67@gmail.com")
		self.assertEqual(self.new_account.passwords,"qwertyui")


#display account list
	def test_dispaly_account(self):
		self.assertEqual(Account.display_accounts(),Account.accounts_list)


if __name__ == "__main__":
	unittest.main()
































# #testing if my credentials are being saved
# 	def test_save_credential(self):
# 		self.new_credential.save_credential()

# 		self.assertEqual(len(Credential.login_credentials),1)

# #tearing Down function to clear class variable
# 	def tearDown(self):
# 		Credential.login_credentials=[]

# #saving multiple credentials 
# 	def test_save_multiple_credentials(self):

# 		self.new_credential.save_credential()

# 		another_credential=Credential("James","Gitau","QWERTY","jamesgitau@gmail.com")
# 		another_credential.save_credential()

# 		self.assertEqual(len(Credential.login_credentials),2)