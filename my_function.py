#days = int(input("days? "))
#amount = int(input("amount? "))

#for n in range(int(days)):
#	amount = amount + amount * .08
#	print(amount)

amount_wanted = int(input("amount wanted? "))

amount = int(input("what is the amount that you will begin with? "))
day = 0
while amount_wanted > amount:
	amount = amount + amount * 0.08
	day += 1

print("It will take you appx " f'{day}' "days")
