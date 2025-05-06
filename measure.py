from utils import read_data
from utils import predict_price

def measure_model_precision(cleaned_data, estimated_price):

	mean_absolute_error = 0
	# Calculate the error size between actual price and estimated price
	for (price, (x, y)) in zip(estimated_price, cleaned_data):
		error = abs(price - y)
		mean_absolute_error += error
	mean_absolute_error = mean_absolute_error / len(cleaned_data)

	return mean_absolute_error

if __name__ == "__main__":

	try:
		cleaned_data = read_data()
		with open('thetas.csv', 'r') as f:
				line = f.read()
		splitted_line = line.split(',')
		thetas_array = []
		thetas_array.append(float(splitted_line[0]))
		thetas_array.append(float(splitted_line[1]))
		estimated_price = predict_price(thetas_array, cleaned_data)
		mean_absolute_error = measure_model_precision(cleaned_data, estimated_price)
		print(f"Mean Absolute Error : {mean_absolute_error}")
	except FileNotFoundError as e:
		print("Wrong file or file path:", e)
	except ValueError as e:
		print("Value error:", e)
	except IndexError as e:
		print("Index error:", e)
	except Exception as e:
		print("An unexpected error occurred:", e)
