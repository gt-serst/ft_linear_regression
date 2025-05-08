# ft_linear_regression
## Subject
### Predict the price of a car according to a single feature : mileage of the car
### The project is separated into two programs:
1. First program predicts the price of a car for a given mileage using this hypothesis:
```math
\text{estimatePrice(mileage)} = \theta_0 + (\theta_1 \times \text{mileage})
```
2. Second trains the model by reading the dataset and performing a linear regression on it using these hypothesis:
```math
\text{tmp}\theta_0 = \text{learningRate} \times \frac{1}{\text{m}} sum_{i = 0}^{m - 1} (\text{estimatePrice(mileage[i] - price[i])})
```
```math
\text{tmp}\theta_1 = \text{learningRate} \times \frac{1}{\text{m}} sum_{i = 0}^{m - 1} (\text{estimatePrice(mileage[i] - price[i])} \times \text{mileage[i]})
```
## A bit of math and logic
### Linear regression
If we plot all the data on a graph, we can see that there is a linear correlation between the points, which can be represented with a straight line. This is called linear regression — a line that accurately represents the data and can be used to predict future values. The equation of this line is a simple function of degree one.
This is the formula for a linear regression:
```math
\text{y} = \theta_0 + \theta_1 \times \text{x}
```
Where:
- y is the target variable (price of a car)
- x is the feature (mileage)
- θ₀ is the bias
- θ₁ is the coefficient
### Loss function
The Loss or Cost function measures how far the model's predictions are from the actual values. In linear regression, it helps us find the line that best fits the data by minimizing this error.
We will use the Mean Absolute Error (MAE):
```math
\text{MAE} = \frac{1}{\text{m}} sum_{i = 1}^{m} |\text{ŷ[i] - y[i]}|
```
Where:
- m is the number of samples
- ŷ is the predicted value
- y is the actual value
### Gradient descent
We calculate two derivatives of the cost function with respect to each parameter. When you have two or more derivatives of the same function, they are called a gradient. We use this gradient to descend to the lowest point in the loss function. The learning rate has an impact on the step size, which corresponds to the amount by which we update the parameters during each iteration of gradient descent.
Here is the two derivatives for each parameter:
```math
\theta_0 = \theta_0 - \alpha \frac{1}{\text{m}} sum_{i = 1}^{m} (\text{ŷ[i] - y[i]})
```
```math
\theta_1 = \theta_1 - \alpha \frac{1}{\text{m}} sum_{i = 1}^{m} ((\text{ŷ[i] - y[i]}) \times \text{x[i]})
```
Where:
- α is the learning rate
- m is the number of samples
- ŷ is the predicted value
- y is the actual value
- x is the feature

The steps to follow are to predict the price of a car based on mileage using a linear regression model with random values for each parameter (θ₀ and θ₁). Then, calculate the mean squared error between the actual values and the predicted values. After that, start the gradient descent by plugging the parameter values into the derivatives and calculating the new parameters that will be used in the next iteration to find the bottom of the cost function curve, which is the optimal point to reduce the error.
