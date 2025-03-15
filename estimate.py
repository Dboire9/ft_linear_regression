import csv
from ft_linear_train import estimate_price
import matplotlib.pyplot as plt

def main():
	input_mileage = input("Please enter a mileage: ")
	print("")
	try:
		input_mileage = int(input_mileage)
		if input_mileage < 0:
			print("Negative mileage is impossible")
			return
	except ValueError as e:
		print(e)
		return
	
	with open('data.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
		data = data[1:]

	mileage = [int(item[0]) for item in data]
	price = [int(item[1]) for item in data]
	
	for _ in range(len(data)):
		plt.scatter(mileage, price)
	
	mileage = normalisation(input_mileage, mileage)
	
	with open('theta_values.csv', newline='') as csvfile:
		theta_data = list(csv.reader(csvfile))
	theta0, theta1 = map(float, theta_data[0])
	if theta0 == 0 and theta1 == 0:
		print("Model has not been trained, please run ft_linear_train.py before launching it")
		return 0

	estimated_price = estimate_price(mileage, theta0, theta1)
	if estimated_price != 0:
		estimated_price = denormalize(estimated_price, price)

	plt.scatter(input_mileage, estimated_price)

	x_values = [-0.1, 1]
	y_values = [estimate_price(x, theta0, theta1) for x in x_values]

	mileage = [int(item[0]) for item in data]
	price = [int(item[1]) for item in data]
	
	x_values[0] = denormalize(x_values[0], mileage)
	x_values[1] = denormalize(x_values[1], mileage)
	y_values[0] = denormalize(y_values[0], price)
	y_values[1] = denormalize(y_values[1], price)

	plt.plot(x_values, y_values, label="Theta Line")
	plt.show()

	print(estimated_price)


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