#Calculator
from colorama import init
init()
from colorama import Fore, Back, Style

print(Fore.BLACK)
print(Back.GREEN)

action = input("Choose the action (+, -, *, /): ")

print(Back.CYAN)
fisrtNumber = input("Input first number: ")
secondNumber = input("Input second number: ")

if action == "+":
	result = float(fisrtNumber) + float(secondNumber)
elif action == "-":
	result = float(fisrtNumber) - float(secondNumber)
elif action == "*":
	result = float(fisrtNumber) * float(secondNumber)
elif action == "/":
	result = float(fisrtNumber) / float(secondNumber)
else:
	result = "Invalid action"

print(Back.YELLOW)
if result == "Invalid action":
	print("Invalid action")
else:
	print("The answer is " + str(result))

input()