import csv
import sys

def main():
	try:
		assert len(sys.argv) == 2, "Please enter only 3 arguments"
		assert sys.argv[1] == "data.csv", "data.csv expected"
	except AssertionError as e:
		print(e)
		return
	theta0 = 0
	theta1 = 0
	print(theta0, theta1)
	file = open("theta_values.py", "w")
	file.write("theta0 = " + str(theta0) + '\n' + "theta1 = " + str(theta1))
	file.close()
	
	with open('data.csv', newline='') as csvfile:
		data = list(csv.reader(csvfile))
	print(data[1][0])
	
	return

if __name__ == "__main__":
	main()