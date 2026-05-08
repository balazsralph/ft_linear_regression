import csv

# Open the theta.csv file and read the theta0 and theta1 values
def read_theta():
	try:
		with open("theta.csv", "r") as file:
			reader = csv.DictReader(file)
			row = next(reader)
			return float(row["theta0"]), float(row["theta1"])
	except (FileNotFoundError, csv.Error):
		print("Error: theta.csv not found")
		exit(1)

# Formula used in the subject
def estimatePrice(mileage):
	theta0, theta1 = read_theta()
	return theta0 + (theta1 * mileage)

# Main function
mileage = input("Enter the mileage: ")
if (not mileage.isdigit()):
	print("Error: Mileage must be a number")
	exit(1)
mileage = float(mileage)
print(f"Estimated price: {estimatePrice(mileage):.2f}")