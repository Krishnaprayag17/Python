binary=str(input("enter a binary number"))
decimal=1
result=0
sum=0
for i in binary:
	sum=int(i)*decimal
	decimal=decimal*2
	result=result+sum
print("decimal value of the binary number",binary,"is ",result)

