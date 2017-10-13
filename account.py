class Account:

	accounts_list=[]

	def __init__(self,emails,passwords):

		self.emails=emails
		self.passwords=passwords



	@classmethod
	def display_accounts(cls):
		return cls.accounts_list

