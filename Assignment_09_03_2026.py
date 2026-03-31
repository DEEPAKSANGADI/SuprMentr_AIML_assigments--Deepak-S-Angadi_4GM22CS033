from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

X = np.array([[1000, 3], [1500, 4], [2000, 5], [2500, 6], [3000, 7]])
y = np.array([200000, 300000, 400000, 500000, 600000])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
print(f"Predictions: {y_pred}")


new_input = np.array([[2200, 5.5]])
predicted_price = model.predict(new_input)
print(f"Predicted price for {new_input[0]}: ${predicted_price[0]:.2f}")