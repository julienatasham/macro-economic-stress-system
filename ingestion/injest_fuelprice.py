import os
import pandas as pd
import yfinance as yf

# Folder path
raw_folder = "data/raw"
os.makedirs(raw_folder, exist_ok=True)

print("Downloading Brent crude prices...")

# Download monthly Brent crude prices
fuel = yf.download("BZ=F", start="2000-01-01", interval="1mo")

fuel = fuel.reset_index()[["Date", "Close"]]
fuel.rename(columns={"Close": "fuel_price_usd"}, inplace=True)

# Save CSV
file_path = os.path.join(raw_folder, "fuelprice.csv")
fuel.to_csv(file_path, index=False)

print("Saved to:", file_path)
print(fuel.head())
