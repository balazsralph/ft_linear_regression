import csv

def load_data(file):
	with open(file, "r") as file:
		reader = csv.DictReader(file)
		return list(reader)

def estimatePrice(theta0, theta1, mileage):
	return 45

def theta0(data, learningRate, m):
	sum = 0;
	theta0 = 0;
	theta1 = 0;
	for i in range(m):
		sum += float(data[i]['price']) - estimatePrice(theta0, theta1, float(data[i]['km']));
	return sum / m;

def theta1(data, learningRate, m):
	sum = 0;
	theta0 = 0;
	theta1 = 0;
	for i in range(m):
		sum += (float(data[i]['price']) - estimatePrice(theta0, theta1, float(data[i]['km'])));
	return sum / m;

### Main function ###
# Read the data from the csv file
data = load_data("data.csv")
if not data:
	print("Error: No data found")
	exit(1)

# Calculate the theta0 and theta1 values
m = len(data);
learningRate = 0.01;
tmpTheta0 = theta0(data, learningRate, m);
tmpTheta1 = theta1(data, learningRate, m);

# Write the theta0 and theta1 values to the csv file
with open("theta.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerow(["theta0", "theta1"])
	writer.writerow([tmpTheta0, tmpTheta1])