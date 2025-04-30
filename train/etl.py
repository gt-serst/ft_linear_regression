def extract_data():

	# Open the file in read mode
	with open('../data.csv', 'r') as f:
		# Read each line in the file
		cleaned_data = []
		for line in f:
		# Get each line
			print(line.strip())
			numbers_array = transform_data(line)
			# Put array with two numbers from the line into a list
			cleaned_data.append(numbers_array)
	return cleaned_data

def transform_data(line):

	# Parse every line except first, get numbers, convert them into integer, scale mileage and put them into an array with two numbers (price and mileage)
	numbers_array = line
	return numbers_array
