class Bank_account:
	def __init__(self):
		self.balance=0
		print("wlcome")
	def deposite(self):
		amount=float(input("Enter the amount to be deposited :"))
		self.balance=self.balance+amount
		print("Amount Deposited \n" "balance :",self.balance)
	def withdraw(self):
		amount=float(input("Enter the amount to be withdrawn :"))
		if(self.balance>=amount):
			self.balance=self.balance-amount
			print("you withdrew",amount)
		else:
			print("insufficent balance")
	def display(self):
		print("your current balance is :",self.balance)
sam=Bank_account()
sam.deposite()
sam.withdraw()
sam.display()
