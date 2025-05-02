import statistics

if __name__ == "__main__":

	with open('../data.csv', 'r') as f:
		mileage_data = []
		for i, line in enumerate(f):
			if i == 0:
				continue
			splitted_line = line.split(',')
			for i in range(len(splitted_line)):
				item = splitted_line[i].strip('\n')
				splitted_line[i] = float(item)
			mileage_data.append(splitted_line[0])
		print(mileage_data)
		mileage_mean = statistics.mean(mileage_data)
		mileage_stdev = statistics.stdev(mileage_data)
	with open('../thetas.csv', 'r') as f:
		line = f.read()
	splitted_line = line.split(',')
	theta_0 = float(splitted_line[0])
	theta_1 = float(splitted_line[1])
	print(theta_0)
	print(theta_1)
	mileage = input("Enter mileage :")
	print(f"Mileage is :{mileage}")
	mileage_scaled = (float(mileage) - mileage_mean) / mileage_stdev
	estimated_price = theta_0 + theta_1 * mileage_scaled
	print(f"Estimated price :{estimated_price}")
