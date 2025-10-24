import basic
import time

intct = basic.Calculator()
loop = 0
result = 0
while (loop != -1):
	if (intct.num == None):
		print("Current value: 0")
	else:
		print(f"Current value: {intct.num}")
	ask = input("What would you like to do? Type add, sub, multi, div, expo, sqrt, log, trig, inv, del to delete, or -1 to quit: ")
	
	if ("-1" in ask):
		loop = -1
	elif ("del" in ask):
		intct.delete()
	elif ("add" in ask or "sum" in "ask"):
		num = float(input("What number would you like to add? (or Type 3.14 for pi or 2.71 for e: "))
		result = intct.sum(num)
		intct.save(result)
	elif ("sub" in ask):
		num = float(input("What number would you like to subtract? (or Type 3.14 for pi or 2.71 for e): "))
		result = intct.subtract(num)
		intct.save(result)
	elif ("multi" in ask):
		result = intct.multiply()
		intct.save(result)
	elif ("div" in ask):
		result = intct.divide()
		intct.save(result)
	elif ("expo" in ask):
		result = intct.expo()
		intct.save(result)
	elif ("sqrt" in ask):
		result = intct.root()
		intct.save(result)
	elif ("trig" in ask):
		result = intct.trig()
	elif ("inv" in ask):
		result = intct.inv()
	elif ("log" in ask):
		result = intct.log()
		intct.save(result)
	else:
		print("That is not an option!")

#py src/index.py