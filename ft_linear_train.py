from ft_linear import estimate_price
import csv
import matplotlib.pyplot as plt

def main():

	with open('data.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
		data = data[1:]

	mileage = [int(item[0]) for item in data]
	print(mileage)
	price = [int(item[1]) for item in data]
	print(price)

	mileage_norm = normalization(mileage)
	price_norm = normalization(price)
	
	mileage = [int(item[0]) for item in data]
	price = [int(item[1]) for item in data]

	for i in range(len(data)):
		plt.scatter(mileage, price)

	epochs = 2000
	learning_rate = 0.1
	calctheta0 = 0
	calctheta1 = 0
	MSE = []
	
	for _ in range(epochs):
		tmp_theta0 = calctheta0 - learning_rate * calculating_tmptheta0(mileage_norm, price_norm)
		tmp_theta1 = calctheta1 - learning_rate * calculating_tmptheta1(mileage_norm, price_norm)
		calctheta0 = tmp_theta0
		calctheta1 = tmp_theta1
		
		file = open("theta_values.csv", "w")
		file.write(str(calctheta0) + ", " + str(calctheta1))
		file.close()

		MSE.append(mean_squared_error(mileage_norm, price_norm))

	x_values = [0, 1]
	y_values = [estimate_price(x) for x in x_values]
	denormalize(x_values, mileage)
	denormalize(y_values, price)

	plt.plot(x_values, y_values, label="Theta Line")
	plt.show()
	
	plt.plot(MSE)
	plt.title("MEAN SQUARED ERROR")
	plt.xlabel("Epoch")
	plt.ylabel("Error")
	plt.show()

	denormalize(mileage_norm, mileage)
	denormalize(price_norm, price)
	return






def mean_squared_error(mileage, price):
	"""Mean squared error function to see the curve of the error in training"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (price[i] - estimate_price(mileage[i])) **2
	return mean / (len(mileage))


def calculating_tmptheta0(mileage, price):
	"""Calulating theta0 as 1/m of m-1∑i=0 (estimatePrice(mileage[i]) - price[i])"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (estimate_price(mileage[i]) - price[i])
	return mean / len(mileage)

def calculating_tmptheta1(mileage, price):
	"""Calulating theta1 as 1/m of m-1∑i=0 (estimatePrice(mileage[i]) - price[i]) * mileage[i]"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (estimate_price(mileage[i]) - price[i]) * mileage[i]
	return mean / len(mileage)





def normalization(array):
	"""Normalization of an array using the min/max normalization x[i] = (x[i] - min_arr) / (max_arr - min_arr))"""
	max_arr = max(array)
	min_arr = min(array)

	for i in range(len(array)):
		array[i] = (array[i] - min_arr) / (max_arr - min_arr)
	return array

def denormalize(array_norm, array):
	"""Denormalization of an array using the min/max denormalization x[i] = x[i] * (max_arr - min_arr) + min_arr"""
	max_arr = max(array)
	min_arr = min(array)

	for i in range(len(array_norm)):
		array_norm[i] = array_norm[i] * (max_arr - min_arr) + min_arr
		# print(array[i])

if __name__ == "__main__":
	main()