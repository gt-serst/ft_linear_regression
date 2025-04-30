def predict_prices(theta_0, theta_1, cleaned_data):

	# Estimate price for every points according to the given theta_0 and theta_1
	estimated_price = []
	for elem in cleaned_data:
		estimated_price = theta_0 + theta_1 * elem[0]
	return estimated_price
