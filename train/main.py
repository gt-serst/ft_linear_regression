from etl import extract_data
from price_prediction import predict_prices
from model_training import calculate_thetas_gradient

if __name__ == "__main__":

	cleaned_data = extract_data()
	thetas_array = [0, 0]
	alpha = 0.05
	gradient_theta_0 = 0
	gradient_theta_1 = 0
	estimated_price = predict_prices(thetas_array, cleaned_data)
	thetas_array = calculate_thetas_gradient(alpha, thetas_array, estimated_price, cleaned_data)
	with open("../thetas.csv", "w") as f:
		f.write(f"{thetas_array[0]},{thetas_array[1]}")
