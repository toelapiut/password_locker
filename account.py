class Account:

	accounts_list=[]

	def __init__(self,emails,passwords):

		self.emails=emails
		self.passwords=passwords



	def save_accounts(self):
		Account.accounts_list.append(self)

	@classmethod
	def display_accounts(cls):
		return cls.accounts_list

