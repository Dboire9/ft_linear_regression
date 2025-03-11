
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
	file = open("theta_values.txt", "w")
	file.write(str(theta0) + " " + str(theta1))
	file.close()
	return

if __name__ == "__main__":
	main()