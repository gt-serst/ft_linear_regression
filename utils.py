# import statistics

def read_data():

	# Read data from the file, read line by line to get the two numbers (price and mileage) and put them individually in integer into an array that will be added to a list
	with open('data.csv', 'r') as f:
		cleaned_data = []
		# mileage_data = []
		# price_data = []
		for i, line in enumerate(f):
			if i == 0:
				continue
			numbers_array = transform_data(line)
			# Put array with two numbers from the line into a list
			# mileage_data.append(numbers_array[0])
			# price_data.append(numbers_array[1])
			cleaned_data.append(numbers_array)
	# cleaned_data = scale_data(mileage_data, price_data)
	return cleaned_data

def transform_data(line):

	# Get every line except first, get numbers, convert them into integer, scale the feature and put them into a two-numbers array
	splitted_line = line.split(',')
	for i in range(len(splitted_line)):
		item = splitted_line[i].strip('\n')
		splitted_line[i] = float(item)
		if (i > 1):
			raise ValueError(f"Line has {i + 1} columns; expected 2.")
		if (splitted_line[i] < 0):
			raise ValueError(f"Negative number not allowed.")
	return splitted_line

# def scale_data(mileage_data, price_data):

# 	mileage_mean = statistics.mean(mileage_data)
# 	mileage_stdev = statistics.stdev(mileage_data)
# 	print(f"mileage_mean: {mileage_mean}")
# 	print(f"mileage_stdev: {mileage_stdev}")
# 	for i in range(len(mileage_data)):
# 		mileage_data[i] = (mileage_data[i] - mileage_mean) / mileage_stdev
# 	merged_data = [[mileage, price] for mileage, price in zip(mileage_data, price_data)]
# 	return merged_data
