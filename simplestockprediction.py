# Import the necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the historical stock price data
stock_prices = np.loadtxt('stock_prices.txt')

# Use the past 10 days of stock prices to predict the next day
X = stock_prices[-10:]
Y = stock_prices[-1]

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, Y)

# Use the model to predict the next day's stock price
next_day_prediction = model.predict(stock_prices[-10:])

# Print the predicted stock price
print(next_day_prediction)


# This code uses a linear regression model to predict the next
# day's stock price based on the past 10 days of stock prices.
# 'It loads the historical stock price data from a file, trains the model on that data,
# 'and then uses the trained model to make a prediction for the next day's stock price.