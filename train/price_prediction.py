def predict_prices(thetas_array, cleaned_data):

	# Estimate price for every points according to the given theta_0 and theta_1
	estimated_price = []
	for elem in cleaned_data:
		estimated_price.append(thetas_array[0] + thetas_array[1] * elem[0])
	return estimated_price
