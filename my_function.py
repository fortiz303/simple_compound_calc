days = int(input("days? "))
amount = int(input("amount? "))

for n in range(int(days)):
	amount = amount + amount * .08
	print(amount)
