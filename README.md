# Stock Price Predictor Using Machine Learning

## Overview

The **Stock Price Predictor** is a Python-based machine learning project that predicts the next trading day's **Opening Price** and **Closing Price** using historical stock market data. The project retrieves real-time historical data from Yahoo Finance using the `yfinance` library and applies the **Linear Regression** algorithm to estimate future stock prices.

## Features

* Downloads real historical stock data from Yahoo Finance.
* Supports both Indian and international stocks.
* Predicts the next day's **Opening Price**.
* Predicts the next day's **Closing Price**.
* Displays historical stock data.
* Visualizes actual and predicted price trends using graphs.
* Allows users to enter any valid Yahoo Finance stock or index symbol.

## Technologies Used

* Python
* yfinance
* Pandas
* Matplotlib
* Scikit-learn (Linear Regression)

## How It Works

1. The user enters a valid Yahoo Finance stock or index symbol.
2. The program downloads historical stock data.
3. The data is preprocessed for machine learning.
4. A Linear Regression model is trained using historical prices.
5. The model predicts the next trading day's opening and closing prices.
6. A graph is displayed showing the historical prices and predicted trend.

## Supported Symbols

### Indian Stocks

* TCS.NS
* RELIANCE.NS
* INFY.NS
* SBIN.NS
* HDFCBANK.NS

### Indian Indices

* ^NSEI (Nifty 50)
* ^NSEBANK (Bank Nifty)
* ^BSESN (Sensex)

### US Stocks

* AAPL
* MSFT
* TSLA
* AMZN
* GOOGL

## Sample Output

```
Downloading stock data...

Model Trained Successfully!

Predicted Next Day Prices
-------------------------
Open Price  : ₹ 2109.34
Close Price : ₹ 2115.82
```

## Project Structure

```
Stock-Price-Predictor/
│
├── stock_predictor.py
├── README.md
└── requirements.txt
```

## Future Enhancements

* Predict High and Low prices.
* Support multiple machine learning algorithms such as Random Forest and LSTM.
* Build a graphical user interface (GUI).
* Develop a web application using Flask or Streamlit.
* Display model accuracy metrics and additional technical indicators.

## Conclusion

This project uses machine learning and real-time Yahoo Finance data to predict the next day's stock opening and closing prices. It demonstrates the basics of data analysis, Linear Regression, and stock market prediction. The project provides a strong foundation for learning more advanced predictive models in the future.

