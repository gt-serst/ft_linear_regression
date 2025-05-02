import matplotlib.pyplot as plt

def plot_data(cleaned_data, estimated_price):

	# Plot data into a graph to see their repartition and the line resulting from the linear regression
	xpoints = get_separate_feature_array(cleaned_data, 0)
	ypoints = get_separate_feature_array(cleaned_data, 1)
	plt.figure(figsize=(12, 8))
	plt.scatter(xpoints, ypoints, label="Actual Data")
	(estimated_price)
	plt.plot(xpoints, estimated_price, color='red', label="Regression Line")
	plt.title("Car Price by Mileage")
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.legend()
	plt.show()

def get_separate_feature_array(cleaned_data, index):

	feature_array = []

	for elem in cleaned_data:
		feature_array.append(elem[index])
	return feature_array
