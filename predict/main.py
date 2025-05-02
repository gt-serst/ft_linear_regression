if __name__ == "__main__":

	with open('../thetas.csv', 'r') as f:
		line = f.read()
	splitted_line = line.split(',')
	theta_0 = float(splitted_line[0])
	theta_1 = float(splitted_line[1])
	print(theta_0)
	print(theta_1)
	mileage = input("Enter mileage :")
	print(f"Mileage is :{mileage}")
	estimated_price = theta_0 + theta_1 * float(mileage)
	print(f"Estimated price :{estimated_price}")
