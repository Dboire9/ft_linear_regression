import csv
import matplotlib.pyplot as plt

def main():

	try: 
		with open('data.csv', newline='') as csvfile:
			data = list(csv.reader(csvfile))
			if not data:
				print("No data found in the csv")
				return
			if data[0][0] != "km" and data[0][1] != "price":
				print("First line of data.csv must be: km,price")
				return
			data = data[1:]
	
	except FileNotFoundError:
		print("Error: 'data.csv' not found.")
		return
	
	except csv.Error as e:
		print(f"Error reading the csv file {e}")
		return

	mileage = [int(item[0]) for item in data]
	price = [int(item[1]) for item in data]

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
		tmp_theta0 = calctheta0 - learning_rate * calculating_tmptheta0(mileage_norm, price_norm, calctheta0, calctheta1)
		tmp_theta1 = calctheta1 - learning_rate * calculating_tmptheta1(mileage_norm, price_norm, calctheta0, calctheta1)
		calctheta0 = tmp_theta0
		calctheta1 = tmp_theta1

		MSE.append(mean_squared_error(mileage_norm, price_norm, calctheta0, calctheta1))
		
	file = open("theta_values.csv", "w")
	file.write(str(calctheta0) + ", " + str(calctheta1))
	file.close()

	x_values = [0, 1]
	y_values = [estimate_price(x,calctheta0, calctheta1) for x in x_values]
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

	print(f"Accuracy of the algorithm using Mean Squared Error {MSE[-1]:.3f}")

	return


def estimate_price(input_mileage, theta0, theta1):
	"""Calculating the hypothesis using θ0 + (θ1 * mileage)"""
	estimated_price = theta0 + (theta1 * float(input_mileage))
	return estimated_price



def mean_squared_error(mileage, price, theta0, theta1):
	"""Mean squared error function to see the curve of the error in training"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (price[i] - estimate_price(mileage[i], theta0, theta1)) **2
	return mean / (len(mileage))


def calculating_tmptheta0(mileage, price, theta0, theta1):
	"""Calulating theta0 as 1/m of m-1∑i=0 (estimatePrice(mileage[i]) - price[i])"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (estimate_price(mileage[i], theta0, theta1) - price[i])
	return mean / len(mileage)

def calculating_tmptheta1(mileage, price, theta0, theta1):
	"""Calulating theta1 as 1/m of m-1∑i=0 (estimatePrice(mileage[i]) - price[i]) * mileage[i]"""
	mean = 0
	for i in range(0, len(mileage)):
		mean += (estimate_price(mileage[i], theta0, theta1) - price[i]) * mileage[i]
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

if __name__ == "__main__":
	main()