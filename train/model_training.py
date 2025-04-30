from price_prediction import price_prediction

def calculate_thetas_gradient(alpha, estimated_price, cleaned_data):

	# Calculate thetas gradient, update thetas then make another price prediction
	for elem in cleaned_data:
		gradient_theta_0 += estimated_price[1] - elem[1]
		gradient_theta_1 += (estimated_price[1] - elem[1]) * elem[0]
	if (gradient_theta_0 < 1 and gradient_theta_1 < 1):
		return thetas_array
	else:
		thetas_array = update_thetas(gradient_theta_0 / len(cleaned_data), gradient_theta_1 / len(cleaned_data) , alpha)
		estimated_price = price_prediction(thetas_array[0], thetas_array[1])
		# Repeat gradient calculation with new estimated_price and thetas update until the loss function converges
		calculate_thetas_gradient(alpha, estimated_price, cleaned_data)

def update_thetas(gradient_theta_0, gradient_theta_1, alpha):

	theta_0 = theta_0 - alpha * gradient_theta_0
	theta_1 = theta_1 - alpha * gradient_theta_1
	return theta_0, theta_1
