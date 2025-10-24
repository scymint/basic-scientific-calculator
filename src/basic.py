#Side project
#by Dyllan Wendhausen
#Created July 10th, 2025
import math



class Calculator:

	def handle(self, value):
		if value == 2.71:
			value = math.e
		elif value == 3.14:
			value = math.pi
		elif value == 6.28:
			value = math.tau
		elif value == None:
			value = 0
		return value
		

	def __init__(self):
		safe = False
		while (safe == False):
			self.num = float(input("Enter a number (or Type 3.14 for pi, 6.28 for 2pi, or 2.71 for e): "))
			if (self.num == 2.71):
				self.num = math.e
				safe = True
			elif (self.num == 3.14):
				self.num = math.pi
				safe = True
			elif (self.num == 6.28):
				self.num = math.tau
				safe = True
			elif self.num == None:
				self.num = 0
				safe = True
			else:
				float(self.num)
				safe = True
			safe = True

	def sum(self, num):
		num = self.handle(num)
		if (self.num == None):
			self.num = 0
		print(f'Adding {self.num} and {num}')
		total = float(self.num + num)
		return total
	def subtract(self, value):
		value = self.handle(value)
		if (self.num == None):
			self.num = 0
		result = 0
		while (result == 0):
			ask = int(input(f"Subtracting {self.num} and {value}. Subtract using {self.num} first or {value} first? (Type 1 or 2): "))
			if (ask == 1 or ask == 2):
				result = ask
				break
			else:
				print("Please type 1 or 2 for the options!")
		if result == 1:
			return self.num - value
		elif result == 2:
			return value - self.num
	def multiply(self):
		num = float(input('Enter the number you want to multiply (or Type 3.14 for pi, 6.28 for 2pi, or 2.71 for e): '))
		if (self.num == None):
			self.num = 0
		num = self.handle(num)
		print(f'Multiplying {self.num} and {num}')
		result = self.num * num
		print(result)
		return result
		
	def divide(self):
		num = float(input("Enter the number you want to divide (or Type 3.14 for pi, 6.28 for 2pi, or 2.71 for e): "))
		if (self.num == None):
			self.num = 0
		num = self.handle(num)
		result = 0
		divide = 0
		if (num/self.num == 1):
			print(f'{self.num} divided by {num} equals 1 ')
			self.num = 1
			return self.num
		elif (num == 0) and (self.num == 0):
			print("Error. Cannot divide nothing by nothing. Try something better like dividing actual numbers.")
		elif (num == 0 and self.num != 0) or (self.num == 0 and num != 0):
			self.num = 0
			print("You thought you were slick but your not. Answer is still 0")
		else:
			while (result == 0):
				ask = int(input(f'Dividing {self.num} and {num}. Divide by {self.num}/{num} or {num}/{self.num}? (Type 1 or 2): '))
				if ask == 1 or ask == 2:
					result = ask
					break
				else:
					print("Please type 1 or 2 for the options!")
			while divide == 0:
				ask = int(input('Include only remainder, rounded, or none? (Type 1,2, or 3): '))
				if ask == 1 or ask == 2 or ask == 3:
					divide = ask
					break
				else:
					print("Please type 1,2, or 3 for the options!")

			if result == 1:
				if divide == 1:
					return self.num%num
				elif divide == 2:
					return self.num//num
				elif divide == 3:
					return self.num/num
			elif result == 2:
				if divide == 1:
					return num%self.num
				elif divide == 2:
					return num//self.num
				elif divide == 3:
					return num/self.num
	def expo(self):
		num = float(input('Enter the number you want to use an exponent on (or Type 3.14 for pi, 6.28 for 2pi, or 2.71 for e): '))
		if (self.num == None):
			self.num = 0
		num = self.handle(num)
		print(f'{self.num} to the power of {num} is:')
		result = self.num ** num
		print(result)
		return result
	def root(self):
		result = 0
		root = 0
		while (root == 0):
			ask = int(input("Would you like to square root or cube root the current number? (Type 1 or 2): "))
			if ask == 1 or ask == 2:
				root = ask
				break
			else:
				print("Please type 1 or 2!")
		if root == 1:
			print(f'Squared root of {self.num} is: ')
			result = math.sqrt(self.num)
		elif root == 2:
			print(f'Cubed root of {self.num} is: ')
			result = math.cbrt(self.num)
		
		return result
	def log(self):
		result = 0
		log = 0
		base = 0
		if (self.num == None):
			self.num = 0
		while (log == 0):
			ask = int(input("Would you like to log base or natural log? (Type 1 or 2): "))
			if (ask == 1):
				log = 1
				break
			elif ask == 2:
				log = 2
				break
			else:
				print("That is not an option!")

		if (log == 1):
			while (base == 0):
				
				ask = float(input("Enter the base for the log: "))

				base = ask
				break
		elif (log == 2):
			base = math.e

		result = math.log(self.num, base)
		print(f'Log {self.num} with the base {base} is {result}')

	def save(self, value):
		self.num = value

	def delete(self):
		confirm = False
		while (confirm == False):
			ask = input("Are you sure you want to do delete your current value? (Type yes or no): ")

			if ("yes" in ask):
				self.num = 0
				print("Number has been reset to 0")
				confirm = True
				
			elif ("no" in ask):
				break
				pass
			else:
				print("That is not a viable option!")
		safe = False
		if confirm == True:
			while (safe == False):
				self.num = float(input("Enter a number (or Type 3.14 for pi, 6.28 for 2pi, or 2.71 for e): "))
				if (self.num == 2.71):
					self.num = math.e
					safe = True
				elif (self.num == 3.14):
					self.num = math.pi
					safe = True
				elif (self.num == 6.28):
					self.num = math.tau
					safe = True
				else:
					float(self.num)
					safe = True
				safe = True
	def trig(self):
		while math.inf:
			ask = input("What trig function would you like to use? (Current options: sin, cos, tan, csc, sec, cot): ")
			if (self.num == None):
				self.num = 0
			if ("cos" in ask):
				print(f'Cosine of {self.num} is: ')
				self.num = math.cos(self.num)
				print(self.num)
				break
			elif "sin" in ask:
				print(f'Sine of {self.num} is: ')
				self.num = math.sin(self.num)
				print(self.num)
				break
			elif "tan" in ask:
				print(f'Tangent of {self.num} is: ')
				self.num = math.tan(self.num)
				print(self.num)
				break
			elif "csc" in ask:
				print(f'Cosecant of {self.num} is: ')
				self.num = 1/(math.sin(self.num))
				print(self.num)
				break
			elif "sec" in ask:
				print(f'Secant of {self.num} is: ')
				self.num = 1/(math.cos(self.num))
				print(self.num)
				break
			elif "cot" in ask:
				print(f'Cotangent of {self.num} is: ')
				self.num = (math.cos(self.num))/(math.sin(self.num))
				print(self.num)
				break
			else:
				print("That is not a viable option!")
	
	def inv(self):
		while math.inf:
			ask = input("What inverse trig function would you like to use? (Current options: sin, cos, tan, csc, sec, cot): ")
			if (self.num == None):
				self.num = 0
			if ("cos" in ask):
				print(f'Arc Cosine of {self.num} is: ')
				self.num = math.acos(self.num)
				print(self.num)
				break
			elif "sin" in ask:
				print(f'Arc Sine of {self.num} is: ')
				self.num = math.asin(self.num)
				print(self.num)
				break
			elif "tan" in ask:
				print(f'Arc Tangent of {self.num} is: ')
				self.num = math.atan(self.num)
				print(self.num)
				break
			elif "csc" in ask:
				print(f'Cosecant of {self.num} is: ')
				self.num = math.asin(1/self.num)
				print(self.num)
				break
			elif "sec" in ask:
				print(f'Secant of {self.num} is: ')
				self.num = math.acos(1/self.num)
				print(self.num)
				break
			elif "cot" in ask:
				print(f'Cotangent of {self.num} is: ')
				self.num = math.atan(1/self.num)
				print(self.num)
				break
			else:
				print("That is not a viable option!")