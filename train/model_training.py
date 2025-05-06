from price_prediction import predict_prices
from model_precision import calculate_model_precision
from visualization import plot_data

def calculate_thetas_gradient(alpha, thetas_array, estimated_price, cleaned_data):

	gradient_theta_0 = 0
	gradient_theta_1 = 0
	# Calculate thetas gradient, update thetas then make another price prediction
	for (price, (x, y)) in zip(estimated_price, cleaned_data):
		# The gradients are the partial derivatives of the Mean Squared Error (MSE) loss function with respect to each parameter: theta_0 is the intercept, theta_1 is the slope
		error = price - y
		gradient_theta_0 += error
		gradient_theta_1 += error * x
	epsilon = 1e-6
	# Stop the model when the partial derivatives with respect to each parameter are very close to zero (when the derivative curve is flat it means that a local minimum is found)
	if abs(gradient_theta_0 / len(cleaned_data)) < epsilon and abs(gradient_theta_1 / len(cleaned_data)) < epsilon:
		# print(f"Last theta 0 computed : {thetas_array[0]}")
		# print(f"Last theta 1 computed : {thetas_array[1]}")
		calculate_model_precision(cleaned_data, estimated_price)
		plot_data(cleaned_data, estimated_price)
		return thetas_array
	else:
		thetas_array = update_thetas(thetas_array, gradient_theta_0 / len(cleaned_data), gradient_theta_1 / len(cleaned_data) , alpha)
		estimated_price = predict_prices(thetas_array, cleaned_data)
		# Repeat gradient calculation with new estimated_price and thetas update until the loss function converges
	return calculate_thetas_gradient(alpha, thetas_array, estimated_price, cleaned_data)

def update_thetas(thetas_array, gradient_theta_0, gradient_theta_1, alpha):

	# Update thetas according to gradients (how far the actual value of thetas are to the optimal value) and alpha (learning rate sensitivity)
	# print(f"Gradient theta 0 : {gradient_theta_0}")
	# print(f"Gradient theta 1 : {gradient_theta_1}")
	thetas_array[0] = thetas_array[0] - alpha * gradient_theta_0
	thetas_array[1] = thetas_array[1] - alpha * gradient_theta_1
	# print(f"New theta 0 computed : {thetas_array[0]}")
	# print(f"New theta 1 computed : {thetas_array[1]}")
	return thetas_array
