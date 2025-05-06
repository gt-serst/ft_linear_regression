from etl import extract_data
from price_prediction import predict_prices
from model_training import calculate_thetas_gradient
import statistics

if __name__ == "__main__":

	try:
		cleaned_data = extract_data()
		thetas_array = [0, 0]
		alpha = 1
		gradient_theta_0 = 0
		gradient_theta_1 = 0
		estimated_price = predict_prices(thetas_array, cleaned_data)
		thetas_array = calculate_thetas_gradient(alpha, thetas_array, estimated_price, cleaned_data)
		with open("../thetas.csv", "w") as f:
			f.write(f"{thetas_array[0]},{thetas_array[1]}")
	except FileNotFoundError as e:
		print("Wrong file or file path:", e)
	except statistics.StatisticsError as e:
		print("Statistics error:", e)
	except ValueError as e:
		print("Value error:", e)
	except IndexError as e:
		print("Index error:", e)
	except Exception as e:
		print("An unexpected error occurred:", e)
