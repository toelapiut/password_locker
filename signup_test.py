import unittest
from locker import Credential

class Test(unittest.TestCase):

	def setUp(self):

		self.new_credential=Credential("apiut","toel","toelapiut7@gmail.com","Hello, This are my notes and hope they work")

	def test_init(self):
		self.assertEqual(self.new_credential.first_name,"apiut")
		self.assertEqual(self.new_credential.last_name,"toel")
		self.assertEqual(self.new_credential.email,"toelapiut7@gmail.com")
		self.assertEqual(self.new_credential.note,"Hello, This are my notes and hope they work")

	def test_save_credential(self):
		self.new_credential.save_credential()

		self.assertEqual(len(Credential.login_credentials),1)



if __name__=="__main__":
	unittest.main(verbosity=2) 