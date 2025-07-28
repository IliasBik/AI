# AI
Model training based on financial market data


Stock Price Prediction using LSTM (MOEX)
This project uses Long Short-Term Memory (LSTM) neural networks to predict future stock prices based on historical data from the Moscow Exchange (MOEX). It includes scripts for data collection, model training, and saved models for inference.

Project Files
API_for_prise.py
A Python script that fetches historical data for a selected stock (by ticker) from the MOEX API. It saves the data in a text file format for training purposes.
Example: Running this script with the ticker SBER will generate SBER.txt.

SBER.txt
A sample data file containing historical price (and possibly volume) information for the Sberbank stock. This file is used as input when training the models.

lstm_model.ipynb
A Jupyter notebook for training an LSTM model using both price and volume as input features. It prepares the data, builds the model using PyTorch, and saves it after training.

lstm_no_value.ipynb
A notebook similar to the one above, but it uses only price data (excluding volume). In testing, this version showed better performance and is generally preferred.

big_model (4).pth
A saved model trained using lstm_no_value.ipynb. It can be loaded with PyTorch for making predictions on new data.

How to Use
Run API_for_prise.py to download historical data for a stock.

Open one of the training notebooks (lstm_model.ipynb or lstm_no_value.ipynb) in Jupyter and follow the steps to train a model using the generated .txt file.

Use the trained .pth model to make predictions on new sequences of historical prices.

Notes
The lstm_no_value version (price-only) generally performs better and is simpler to train.

Models are built using PyTorch and can be easily extended or adjusted.

To test the models, use stock_simulator.ipynb and data from one of the assets (for example MOEX_short.txt ). The code selects a random point in time, loads the last few prices into the model, and gets the next price predicted by the model. Next, the program loads the last predicted price into the model and receives a new prediction. This continues until the predictions reach the desired length. Next, the program puts prices on the chart so that you can compare the prediction and reality.
