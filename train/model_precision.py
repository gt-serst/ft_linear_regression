def calculate_model_precision(cleaned_data, estimated_price):

	mean_absolute_error = 0
	# Calculate the error size between actual price and estimated price
	for (price, (x, y)) in zip(estimated_price, cleaned_data):
		error = abs(price - y)
		mean_absolute_error += error
	mean_absolute_error = mean_absolute_error / len(cleaned_data)
	# print(f"Mean Absolute Error : {mean_absolute_error}")

	return mean_absolute_error
