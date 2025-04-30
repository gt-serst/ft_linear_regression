if __name__ == "__main__":

	with open('../thetas.csv', 'r') as f:
		theta_0 = f.read()
		theta_1 = f.read()
	mileage = input("Enter mileage :")
	print("Mileage is :" + mileage)
	estimated_price = theta_0 + theta_1 * mileage
	print("Estimated price :" + estimated_price)
