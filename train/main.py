from etl import extract_data
from price_prediction import predict_prices
from model_training import calculate_thetas_gradient

if __name__ == "__main__":

	cleaned_data = extract_data()
	theta_0 = 0
	theta_1 = 0
	alpha = 0.05
	estimated_price = predict_prices(theta_0, theta_1, cleaned_data)
	thetas_array = calculate_thetas_gradient(alpha, estimated_price, cleaned_data)
	with open("../thetas.csv", "w") as f:
		f.write(thetas_array)
