import csv

def main():
	mileage = input("Please enter a mileage: ")
	print("")
	try:
		int(mileage)
	except ValueError as e:
		print(e)
		return
	
	print(estimate_price(mileage))
	

def estimate_price(mileage: int) -> int:
	with open('theta_values.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
	estimate_price = float(data[0][0]) + (float(data[0][1]) * float(mileage))
	print(estimate_price)
	return estimate_price


if __name__ == "__main__":
	main()