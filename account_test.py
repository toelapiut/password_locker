import unittest
from account import Account


class Tests(unittest.TestCase):


#set up 
	def setUp(self):

		self.new_account=Account("jamesgitau67@gmail.com","qwertyui")

#creation of an initializing test 
	def test_init(self):
		self.assertEqual(self.new_account.emails,"jamesgitau67@gmail.com")
		self.assertEqual(self.new_account.passwords,"qwertyui")

#save accounts 
	def test_save_accounts(self):
		self.new_account.save_accounts()
		self.assertEqual(len(Account.accounts_list),1)

#tear down clears everything
	def tearDown(self):
		Account.accounts_list=[]

#save multiple contacts
	def test_save_multiple_accounts(self):
		self.new_account.save_accounts()

		test_account=Account("james6@gmail.com","qwe123")
		test_account.save_accounts()
		self.assertEqual(len(Account.accounts_list),2)

#display account list
	def test_dispaly_account(self):
		self.assertEqual(Account.display_accounts(),Account.accounts_list)


if __name__ == "__main__":
	unittest.main()






























