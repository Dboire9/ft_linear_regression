import csv

def main():
	input_mileage = input("Please enter a mileage: ")
	print("")
	try:
		input_mileage = int(input_mileage)
	except ValueError as e:
		print(e)
		return
	
	with open('data.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
		data = data[1:]

	mileage = [int(item[0]) for item in data]
	price = [int(item[1]) for item in data]
	
	mileage = normalisation(input_mileage, mileage)
	estimated_price = estimate_price(mileage)
	if estimated_price != 0:
		estimated_price = denormalize(estimated_price, price)

	print(estimated_price)

def estimate_price(input_mileage):
	with open('theta_values.csv', newline='') as csvfile:
		theta_data = list(csv.reader(csvfile))
	
	theta0, theta1 = map(float, theta_data[0])

	if theta0 == 0 and theta1 == 0:
		print("Model has not been trained, please run ft_linear_train.py before launching it")
		return 0
	estimated_price = theta0 + (theta1 * float(input_mileage))
	return estimated_price

def denormalize(theta, array):
	max_arr = max(array)
	min_arr = min(array)

	theta = theta * (max_arr - min_arr) + min_arr
	return theta

def normalisation(mileage_input, array):
	max_arr = max(array)
	min_arr = min(array)

	mileage_input = (mileage_input - min_arr) / (max_arr - min_arr)
	return mileage_input


if __name__ == "__main__":
	main()