class bank_accnt:

	def __init__(self):
		self.balance=0
		
	def deposit(self):
		deposit_amnt=int(input("enter the amount to deposit"))
		self.balance+=deposit_amnt
		print("current blance",self.balance)
		
	def withdraw(self):
		withdraw_amnt=int(input("enter the amount to withdraw"))
		if withdraw_amnt>self.balance:
			print("Insufficient Balance")
		else:
			self.balance-=withdraw_amnt
			print("Balance is ",self.balance)
	def display(self):
		print("Balance amount is ",self.balance)
		
my_accnt=bank_accnt()
my_accnt.deposit()
my_accnt.withdraw()
my_accnt.display() 	
my_accnt.withdraw()
