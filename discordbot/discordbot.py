# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:41:23 2023

@author: shemar
"""

import discord 
import yfinance as yf

BotToken = 'MTEyMzM0NDYxMjYwMjQxMzA4Ng.G6NkV2.Mg5iWvjQQTaFc4LNGbwc31QMhBOXJQVTDQW48A'

# Define intents
intents = discord.Intents.default()

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

        # Use yfinance to get the stock data
        stock = yf.Ticker(symbol)

    try:
        # Get stock info
        stock_info = stock.info
        # Send a message back to the channel with the stock price 
        await message.channel.send(f'The price of {symbol} is {stock_info["currentPrice"]}')
    except Exception as e:
        print(e)  # This will print the full error message to your console
        await message.channel.send(f'Unable to get the price for {symbol}. Please ensure the stock symbol is correct.')
    
# Run the client with your bot token
client.run(BotToken)
