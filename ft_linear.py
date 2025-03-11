from ft_linear_train import *
import sys

def main():
	mileage = input("Please enter a mileage: ")
	print("")
	try:
		int(mileage)
	except ValueError as e:
		print(e)
		return

if __name__ == "__main__":
	main()