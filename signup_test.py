import unittest
from locker import Credential

class Test(unittest.TestCase):

	def setUp(self):

		self.new_credential("apiut","toel","toelapiut7@gmail.com","Hello, This are my notes and hope they work")

		self.assertEqual(self.new_credential.first_name,"apiut")
		self.assertEqual(self.new_credential.last_name,"toel")
		self.assertEqual(self.new_credential.email,"toelapiut7@gmail.com")
		self.assertEqual(self.new_credential.notes,"This are my notes and hope they work")



if __name__=="__main__":
	unittest.main(verbosity=0)