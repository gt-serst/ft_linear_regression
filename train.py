from utils import read_data
from utils import predict_price
from model import calculate_thetas_gradient

def scale_data(cleaned_data):

	scaled_data = []
	mileage_mean = 0
	mileage_stdev = 0
	for elem in cleaned_data:
		mileage_mean += elem[0]
	mileage_mean /= len(cleaned_data)
	for elem in cleaned_data:
		mileage_stdev += (elem[0] - mileage_mean) ** 2
	mileage_stdev = (mileage_stdev / len(cleaned_data)) ** 0.5
	for elem in cleaned_data:
		scaled_mileage = (elem[0] - mileage_mean) / mileage_stdev
		scaled_data.append([scaled_mileage, elem[1]])

	return scaled_data

if __name__ == "__main__":

	try:
		cleaned_data = read_data()
		scaled_data = scale_data(cleaned_data)
		thetas_array = [0, 0]
		alpha = 1
		estimated_price = predict_price(thetas_array, scaled_data)
		thetas_array = calculate_thetas_gradient(alpha, thetas_array, estimated_price, scaled_data, cleaned_data)
		with open("thetas.csv", "w") as f:
			f.write(f"{thetas_array[0]},{thetas_array[1]}")
	except FileNotFoundError as e:
		print("Wrong file or file path:", e)
	except ValueError as e:
		print("Value error:", e)
	except IndexError as e:
		print("Index error:", e)
	except ZeroDivisionError as e:
		print("Zero division error:", e)
	except Exception as e:
		print("An unexpected error occurred:", e)
