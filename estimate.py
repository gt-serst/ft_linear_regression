if __name__ == "__main__":

	try:
		with open('thetas.csv', 'r') as f:
			line = f.read()
		splitted_line = line.split(',')
		theta_0 = float(splitted_line[0])
		theta_1 = float(splitted_line[1])
		mileage = input("Enter mileage : ")
		estimated_price = theta_0 + theta_1 * float(mileage)
		print(f"Estimated price : {estimated_price}")
	except FileNotFoundError as e:
		print("Wrong file or file path:", e)
	except ValueError as e:
		print("Value error:", e)
	except IndexError as e:
		print("Index error:", e)
	except Exception as e:
		print("An unexpected error occurred:", e)
