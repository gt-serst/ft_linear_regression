def read_data():

	# Read data from the file, read line by line to get the two numbers (price and mileage) and put them individually in integer into an array that will be added to a list
	with open('perfect_data.csv', 'r') as f:
		cleaned_data = []
		for i, line in enumerate(f):
			if i == 0:
				continue
			numbers_array = get_numbers(line)
			# Put array with two numbers from the line into a list
			cleaned_data.append(numbers_array)
	return cleaned_data

def get_numbers(line):

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

def predict_price(thetas_array, cleaned_data):

	# Estimate price for every points according to the given theta_0 and theta_1
	estimated_price = []
	for elem in cleaned_data:
		estimated_price.append(thetas_array[0] + thetas_array[1] * elem[0])
	return estimated_price
