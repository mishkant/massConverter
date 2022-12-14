unit = input("Tones or Kilograms? ")
amount = float(input("Amount: "))

if unit == "Tones":
	print(f"{amount * 1000} Kg.")

elif unit == "Kilograms":
	print(f"{amount / 1000} Kg.")

else:
	print("Oh no!! Error!")
	