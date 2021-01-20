
import os
import math
from decimal import Decimal

	
def Home():
	while True:
		print("""

			1) Find the hypotnuse
			
			2) Find the side a
			
			3) Find the side b

			4) Exit



			""")
		root = input("Choose: ")
		if root == "1":
			os.system("cls")
			def Values_1():
				global value_b
				global value_a

				try:
					print()
					value_a = int(input("Enter the value of side a: "))
				except(ValueError):
					print()
					print("Please enter a number")
					return Values_1()
				try:
					print()
					value_b = int(input("Enter the value of side b: "))

				except(ValueError):
					print("Please enter a number")
					return Values_1()
			Values_1()		
			print("a² + b² = c²")
			value = value_a * value_a 
			value2 = value_b * value_b
			print(value, "+", value2, "=", "c²")
			print()
			print(value + value2, "=", "c²")
			total = value + value2
			print()
			square_root = total ** 0.5
			print()			
			print(f"{square_root:.2f}")

		if root == "2":
			os.system("cls")
			def Values():
				global hyp2
				global side_a
				try:
					hyp2 = int(input("Enter the value of hypotnuse: "))
				except(ValueError):
					print()
					print("Please enter a number")
				try:
					print()
					side_a = int(input("Enter the value of side b: "))
				except(ValueError):
					print()
					print("Please enter a number")

				if side_a > hyp2:
					print("Side cannot be greater then hypotnuse")
					return Values()
				if side_a < hyp2:
					print("a² + b² = c²")
					print()
					print("a²", "+", f"{side_a}² =", f"{hyp2}²")
					print()
					print("a²", "+", side_a * side_a, "=", hyp2 * hyp2)
					print()
					value4 = side_a * side_a
					value5 = hyp2 * hyp2 
					print("a²", "=", f"{value5} " "- " f"{value4}")
					print()
					print("a²", "=", value5-value4)
					print()
					total2 = value5-value4
					square_root2 = total2 ** 0.5
					print()
					print(f"{square_root2:.2f}")


				if side_a == hyp2:
					print()
					print("Side cannot be the similar as the hypotnuse it has to be smaller")
					return Values()
			
			Values()

	
		if root == "3":
			os.system("cls")
			def Values2():
				global hyp3
				global side_b
				try:
					print()
					hyp3 = int(input("Enter the value of hypotnuse: "))
	  				
				except(ValueError):
					print()
					print("Please enter a number")
					return Values2()
				try:
					print()
					side_b = int(input("Enter the value of side b: "))
				except(ValueError):
					print()
					print("Please enter a number")
					return Values2()

				if side_b > hyp3:
					print()
					print("Side cannot be greater then hypotnuse")
				
				if side_b == hyp3:
					print()
					print("Side cannot be the similar as the hypotnuse it has to be smaller")
					return Values2()

				if side_b < hyp3:
					print("a² + b² = c²")
					print()
					print("a²", "+", f"{side_b}² =", f"{hyp3}²")
					print()
					print("a²", "+", side_b * side_b, "=", hyp3 * hyp3)
					print()
					value6 = side_b * side_b
					value7 = hyp3 * hyp3 
					print("a²", "=", f"{value7}", "- " f"{value6}")
					print()
					print("a²", "=", value7-value6)
					total3 = value7-value6
					square_root3 = total3 ** 0.5
					print()
					print("a = "f"{square_root3:.2f}")
					
			Values2()		

		if root == "4":
			print("Bye...")	
			exit()	

		if root == "cls":
			os.system("cls")
		
Home()
