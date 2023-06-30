# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:41:23 2023

@author: shemar
"""

import discord 
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

BotToken = 'Token'

# Define intents
intents = discord.Intents.default()
intents.guild_messages = True

# Create a client instance with the defined intents
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # if the bot sends the message, ignore it
    if message.author == client.user:
        return

    # if the message starts with '$stockprice'
    if message.content.startswith('$stockprice'):
        
        # Check if a stock symbol was given
        msg_parts = message.content.split(" ", 1)
        if len(msg_parts) <= 1:
            await message.channel.send('Please provide a stock symbol.')
            return
        # Extract the stock symbol from the message
        symbol = msg_parts[1]
        
        # Initialize stock to None
        stock = None
    try:
        # Use yfinance to get the stock data
        stock = yf.Ticker(symbol)
        
        #Get the historical market data
        end = datetime.today().strftime('%Y-%m-%d')
        start = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
        hist = stock.history(start=start, end=end)
        
        # Fit a linear regression model to the data
        model = LinearRegression()
        model.fit(np.array(range(len(hist))).reshape(-1,1), hist["Close"].values)

        # Get stock info
        stock_info = stock.info
        
        #create a plot 
        plt.figure(figsize=(10, 5))
        plt.plot(hist["Close"].values, label='Closing Price')
        plt.plot(model.predict(np.array(range(len(hist))).reshape(-1, 1)), label='Trend Line')
        plt.title(f'{symbol} Closing Price vs Trend Line')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        #save the plot to a file
        
        plt.savefig('LinearStockGraph.png')
        plt.close()
        
        # Determine if the slope is positive or negative
        slope_direction = 'up' if model.coef_[0] >= 0 else 'down'
        
        # Send a message back to the channel with the stock price 
        await message.channel.send(f'The price of {symbol} is {stock_info["currentPrice"]}')
        await message.channel.send(f'The linear regression slope for the past 30 days of {symbol} is {model.coef_[0]:.4f}, indicating a trend {slope_direction}.')
        #send the plot to the channel
        await message.channel.send(file=discord.File('plot.png'))
    except Exception as e:
        print(e)  # This will print the full error message to your console
        await message.channel.send(f'Unable to get the price for {symbol}. Please ensure the stock symbol is correct.')
    
# Run the client with your bot token
client.run(BotToken)
