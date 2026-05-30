import csv

########################################################
# Functions
########################################################

def estimatePrice(theta0, theta1, mileage):
	return theta0 + (theta1 * mileage)

########################################################
# Main function
########################################################

if __name__ == "__main__":
	#### Load the theta.csv from train.py
	try:
		with open("theta.csv", "r") as file:
			row = next(csv.DictReader(file))
			theta0 = float(row["theta0"])
			theta1 = float(row["theta1"])
	except (FileNotFoundError, StopIteration, csv.Error, KeyError, ValueError):
		print("Error: theta.csv not found or invalid")
		theta0, theta1 = 0.0, 0.0

	#### Get the mileage from the user
	try:
		mileage = float(input("Enter the mileage: "))
	except ValueError:
		print("Error: Mileage must be a number")
		exit(1)

	#### Result
	print(f"Estimated price: {estimatePrice(theta0, theta1, mileage):.2f}")