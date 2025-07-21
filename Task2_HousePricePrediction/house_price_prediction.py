import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("house_prices.csv")
X = df[['Rooms', 'Size']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)
plt.scatter(df['Size'], y, color='blue', label='Actual')
plt.scatter(df['Size'], predicted, color='red', label='Predicted')
plt.xlabel('Size (sqft)')
plt.ylabel('Price')
plt.title('House Size vs Price')
plt.legend()
plt.show()

print("Predicted prices:")
print(predicted)
