# import statistics

if __name__ == "__main__":

	try:
		# with open('data.csv', 'r') as f:
		# 	mileage_data = []
		# 	for i, line in enumerate(f):
		# 		if i == 0:
		# 			continue
		# 		splitted_line = line.split(',')
		# 		for i in range(len(splitted_line)):
		# 			item = splitted_line[i].strip('\n')
		# 			splitted_line[i] = float(item)
		# 			if (i > 1):
		# 				raise ValueError(f"Line has {i + 1} columns; expected 2.")
		# 			if (splitted_line[i] < 0):
		# 				raise ValueError(f"Negative number not allowed.")
		# 		mileage_data.append(splitted_line[0])
		# 	mileage_mean = statistics.mean(mileage_data)
		# 	mileage_stdev = statistics.stdev(mileage_data)
		with open('thetas.csv', 'r') as f:
			line = f.read()
		splitted_line = line.split(',')
		theta_0 = float(splitted_line[0])
		theta_1 = float(splitted_line[1])
		mileage = input("Enter mileage : ")
		if (theta_0 == 0 and theta_1 == 0):
			print(f"Estimated price : 0")
		else:
			# mileage_scaled = (float(mileage) - mileage_mean) / mileage_stdev
			# estimated_price = theta_0 + theta_1 * mileage_scaled
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
