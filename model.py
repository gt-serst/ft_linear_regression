from predict import predict_price
# from model_precision import calculate_model_precision
from plot import plot_data

def calculate_thetas_gradient(alpha, thetas_array, estimated_price, scaled_data, cleaned_data):

	gradient_theta_0 = 0
	gradient_theta_1 = 0
	# Calculate thetas gradient, update thetas then make another price prediction
	for (price, (x, y)) in zip(estimated_price, scaled_data):
		# The gradients are the partial derivatives of the Mean Squared Error (MSE) loss function with respect to each parameter: theta_0 is the intercept, theta_1 is the slope
		error = price - y
		gradient_theta_0 += error
		gradient_theta_1 += error * x
	epsilon = 1e-6
	# Stop the model when the partial derivatives with respect to each parameter are very close to zero (when the derivative curve is flat it means that a local minimum is found)
	if abs(gradient_theta_0 / len(scaled_data)) < epsilon and abs(gradient_theta_1 / len(scaled_data)) < epsilon:
		# print(f"Last theta 0 computed : {thetas_array[0]}")
		# print(f"Last theta 1 computed : {thetas_array[1]}")
		# calculate_model_precision(scaled_data, estimated_price)
		thetas_array = unscale_thetas(thetas_array, cleaned_data)
		print(thetas_array)
		estimated_price = predict_price(thetas_array, cleaned_data)
		plot_data(cleaned_data, estimated_price)
		return thetas_array
	else:
		thetas_array = update_thetas(thetas_array, gradient_theta_0 / len(scaled_data), gradient_theta_1 / len(scaled_data) , alpha)
		estimated_price = predict_price(thetas_array, scaled_data)
		# Repeat gradient calculation with new estimated_price and thetas update until the loss function converges
	return calculate_thetas_gradient(alpha, thetas_array, estimated_price, scaled_data, cleaned_data)

def update_thetas(thetas_array, gradient_theta_0, gradient_theta_1, alpha):

	# Update thetas according to gradients (how far the actual value of thetas are to the optimal value) and alpha (learning rate sensitivity)
	# print(f"Gradient theta 0 : {gradient_theta_0}")
	# print(f"Gradient theta 1 : {gradient_theta_1}")
	thetas_array[0] = thetas_array[0] - alpha * gradient_theta_0
	thetas_array[1] = thetas_array[1] - alpha * gradient_theta_1
	# print(f"New theta 0 computed : {thetas_array[0]}")
	# print(f"New theta 1 computed : {thetas_array[1]}")
	return thetas_array

def unscale_thetas(thetas_array, cleaned_data):

	mileage_mean = 0
	mileage_stdev = 0
	for elem in cleaned_data:
		mileage_mean += elem[0]
	mileage_mean /= len(cleaned_data)
	print(f"mileage_mean: {mileage_mean}")
	for elem in cleaned_data:
		mileage_stdev += (elem[0] - mileage_mean) ** 2
	mileage_stdev = (mileage_stdev / len(cleaned_data)) ** 0.5
	print(f"mileage_stdev: {mileage_stdev}")
	# To found these formulas substitute the scaled x by the formulas used to scale it in the linear regression equation
	thetas_array[1] = thetas_array[1] / mileage_stdev
	thetas_array[0] = thetas_array[0] - (thetas_array[1] * mileage_mean)
	print(f"thetas_array[0]: {thetas_array[0]}")
	print(f"thetas_array[1]: {thetas_array[1]}")
	return thetas_array

