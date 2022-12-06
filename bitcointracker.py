import requests
from tkinter import *

# Define the API endpoint for the Coinbase API
url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

# Create a new Tkinter window
window = Tk()
window.title("Bitcoin Price")
window.geometry("800x600")
window["bg"] = "black"


# Create a label to display the Bitcoin price
price_label = Label(window, text="Loading...", fg="white", bg="black")
price_label.pack()
# Define a function that updates the Bitcoin price
def update_price():
    # Use the requests library to make a GET request to the API endpoint
    response = requests.get(url)

    # Extract the Bitcoin price from the API response
    price = response.json()["data"]["amount"]

    # Update the label with the live Bitcoin price
    price_label.config(text=price)

    # Schedule the update_price() function to be called again after 1 second
    window.after(5000, update_price)

# Call the update_price() function to display the initial Bitcoin price
update_price()

# Run the Tkinter event loop
window.mainloop()
#%%
