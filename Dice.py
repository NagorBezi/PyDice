import keyboard
import random

keyboard.wait("SPACE")
dice_face = random.randint(1, 6)

if str(dice_face) == '1':
	print("---------")
	print("|       |")
	print("|   O   |")
	print("|       |")
	print("---------")

if str(dice_face) == '2':
	print("---------")
	print("|       |")
	print("| O   O |")
	print("|       |")
	print("---------")

if str(dice_face) == '3':
	print("---------")
	print("|     O |")
	print("|   O   |")
	print("| O     |")
	print("---------")

if str(dice_face) == '4':
	print("---------")
	print("| O   O |")
	print("|       |")
	print("| O   O |")
	print("---------")

if str(dice_face) == '5':
	print("---------")
	print("| O   O |")
	print("|   O   |")
	print("| O   O |")
	print("---------")

if str(dice_face) == '6':
	print("---------")
	print("| O   O |")
	print("| O   O |")
	print("| O   O |")
	print("---------")
