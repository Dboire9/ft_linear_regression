from theta_values import theta0, theta1

def main():
	mileage = input("Please enter a mileage: ")
	print("")
	try:
		int(mileage)
	except ValueError as e:
		print(e)
		return
def price_estimation(mileage: int):
	estimate_price = int(theta0) + (int(theta1) * int(mileage))
	return
if __name__ == "__main__":
	main()