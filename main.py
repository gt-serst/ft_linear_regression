from etl import extract_data
from price_prediction import price_prediction
from model_training import calculate_average_error

if __name__ == "__main__":

	cleaned_data = extract_data()
	theta_0 = 0
	theta_1 = 0
	estimated_price = price_prediction(theta_0, theta_1, cleaned_data)
	calculate_average_error(estimated_price)
