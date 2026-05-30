import csv
from predictPrice import estimatePrice

########################################################
# Functions
########################################################

# Theta0 = Origin y axis
def compute_tmp_theta0(data, learning_rate, m, theta0, theta1, max_km, max_price):
	sum = 0
	for i in range(m):
		mileage = float(data[i]['km']) / max_km
		price = float(data[i]['price']) / max_price
		sum += estimatePrice(theta0, theta1, mileage) - price
	return learning_rate * (sum / m)

# Theta1 = Linear coefficient
def compute_tmp_theta1(data, learning_rate, m, theta0, theta1, max_km, max_price):
	sum = 0
	for i in range(m):
		mileage = float(data[i]['km']) / max_km
		price = float(data[i]['price']) / max_price
		sum += (estimatePrice(theta0, theta1, mileage) - price) * mileage
	return learning_rate * (sum / m)


########################################################
# Main function
########################################################

if __name__ == "__main__":
	#### Load the data
	try:
		with open("data.csv", "r") as file:
			data = list(csv.DictReader(file))
	except FileNotFoundError:
		print("Error: data.csv not found")
		exit(1)

	#### Initialize the variables
	m = len(data)
	max_km = max(float(row['km']) for row in data)
	max_price = max(float(row['price']) for row in data)
	learning_rate = 0.01
	theta0, theta1 = 0.0, 0.0

	#### Train the model
	while True:
		tmp_theta0 = compute_tmp_theta0(data, learning_rate, m, theta0, theta1, max_km, max_price)
		tmp_theta1 = compute_tmp_theta1(data, learning_rate, m, theta0, theta1, max_km, max_price)
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
		print(f"theta0: {theta0}, theta1: {theta1}")
		if abs(tmp_theta0) < 1e-10 and abs(tmp_theta1) < 1e-10:
			break
	theta0 *= max_price
	theta1 *= max_price / max_km


	#### Create the theta.csv file
	with open("theta.csv", "w") as file:
		writer = csv.writer(file)
		writer.writerow(["theta0", "theta1"])
		writer.writerow([theta0, theta1])

	print("\033[92mTraining completed successfully\033[0m")