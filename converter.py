
print('Mariam Razmadze')


unit = input("T or KG? ")
amount = float(input("Amount: "))

if unit == "Tone":
	print(f"{amount * 1000} Kg.")

elif unit == "KiloGrams":
	print(f"{amount / 1000} Kg.")

else:
	print("Oh no! Error!")
	