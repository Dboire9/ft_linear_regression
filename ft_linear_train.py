from ft_linear import estimate_price
import csv
import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
	# try:
	# 	assert len(sys.argv) == 2, "Please enter only 3 arguments"
	# 	assert sys.argv[1] == "data.csv", "data.csv expected"
	# except AssertionError as e:
	# 	print(e)
	# 	return

	with open('data.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
		data = data[1:]
	data = normalisation(data)
	for i in range(len(data)):
		plt.scatter(data[i][0], data[i][1])
	# mean_squared_error(data)
	with open('theta_values.csv', newline='') as csvfile:
		data_theta = list(csv.reader(csvfile))
	epochs = 1000
	for i in range(0, epochs):
		linear_regression(data)
		plt.plot([float(data_theta[0][0]), float(data_theta[0][1])])
	plt.show()
	return

def mean_squared_error(data):
	mean = 0
	for i in range(1, len(data)):
		mean = mean + pow((float(data[i][1]) - estimate_price(data[i][0])), 2)
		i += 1
	mean = mean / (len(data) - 1)
	return mean

def linear_regression(data):
	learning_rate = 0.1
	with open('theta_values.csv', newline='') as csvfile:
		data_theta = list(csv.reader(csvfile))
	calctheta0 = calculating_tmptheta0(data)
	calctheta1 = calculating_tmptheta1(data)
	tmptheta0 = float(data_theta[0][0]) - learning_rate * calctheta0
	tmptheta1 = float(data_theta[0][1]) - learning_rate * calctheta1
	print(tmptheta0)
	print(tmptheta1)
	file = open("theta_values.csv", "w")
	file.write(str(tmptheta0) + ", " + str(tmptheta1))
	file.close()


def calculating_tmptheta0(data):
	mean = 0
	for i in range(1, len(data)):
		mean = mean + (estimate_price(data[i][0]) - float(data[i][1]))
	mean = mean / (len(data))
	return mean

def calculating_tmptheta1(data):
	mean = 0
	for i in range(1, len(data)):
		mean = mean + ((estimate_price(data[i][0]) - float(data[i][1])) * float(data[i][0]))
	mean = mean / (len(data))
	return mean
	
def normalisation(data):
	max_x = 0
	max_y = 0
	for i in range(len(data)):
		if(float(data[i][0]) > max_x):
			max_x = float(data[i][0])
		if(float(data[i][1]) > max_y):
			max_y = float(data[i][1])
			
	min_x = max_x
	min_y = max_y
	for i in range(len(data)):
		if(float(data[i][0]) < min_x):
			min_x = float(data[i][0])
		if(float(data[i][1]) < min_y):
			min_y = float(data[i][1])
	
	print(max_x, max_y)
	print(min_x, min_y)
	for i in range(len(data)):
		data[i][0] = (float(data[i][0]) - min_x) / (max_x - min_x)
		data[i][1] = (float(data[i][1]) - min_y) / (max_y - min_y)
		print(data[i][0], data[i][1])
	return data
	

if __name__ == "__main__":
	main()