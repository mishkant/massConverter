

print("Welcome to this game")
prin("10:02")

unit = input("T or KG? ")
amount = float(input("Amount: "))

if unit == "T":
	print(f"{amount * 1000} Kg.")

elif unit == "KG":
	print(f"{amount / 1000} Kg.")

else:
	print("Error!")
	print("Hello World")
 print("Bye Bye")