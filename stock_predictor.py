import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# STEP 1: Download Real Stock Data
stock_symbol = input("Enter Stock/Index Symbol: ") 
print("Downloading stock data...")

stock_data = yf.download(
    stock_symbol,
    start="2026-06-19",
    end="2026-06-26"
)

print("\nFirst 5 Rows:")
print(stock_data.head())

# STEP 2: Prepare Close Price Data
close_data = stock_data[['Close']].copy()
close_data['Day'] = range(len(close_data))

X_close = close_data[['Day']]
y_close = close_data['Close']

# STEP 3: Train Close Price Model
close_model = LinearRegression()
close_model.fit(X_close, y_close)

print("\nModel Trained Successfully!")

# STEP 4: Predict Next Day Close Price
next_day = [[len(close_data)]]

predicted_close = close_model.predict(next_day)

# STEP 5: Predict Next Day Open Price
open_data = stock_data[['Open']].copy()
open_data['Day'] = range(len(open_data))

X_open = open_data[['Day']]
y_open = open_data['Open']

open_model = LinearRegression()
open_model.fit(X_open, y_open)

predicted_open = open_model.predict(next_day)

print("\nPredicted Next Day Prices")
print("-------------------------")
print(f"Open Price  : ₹ {predicted_open[0][0]:.2f}")
print(f"Close Price : ₹ {predicted_close[0][0]:.2f}")

# STEP 6: Plot Graph
predicted_values = close_model.predict(X_close)

plt.figure(figsize=(10, 5))

plt.plot(
    close_data['Day'],
    y_close,
    label="Actual Close Price"
)

plt.plot(
    close_data['Day'],
    predicted_values,
    label="Predicted Close Trend"
)

plt.title("Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price (₹)")
plt.legend()

plt.grid(True)
plt.show()