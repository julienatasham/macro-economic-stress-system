import pandas as pd
import os
import yfinance as yf

# 1️⃣ Set up folders (relative to project)
raw_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")
os.makedirs(raw_folder, exist_ok=True)
output_file = os.path.join(raw_folder, "fx.csv")

# 2️⃣ Download USD/KES historical data
fx_ticker = "USDKES=X"
df = yf.download(fx_ticker, start="2000-01-01", end="2025-12-31")
df = df.reset_index()
df = df[['Date', 'Close']]  # Keep date and closing rate
df.rename(columns={'Close': 'fx_kes_usd'}, inplace=True)

# 3️⃣ Save to raw folder
df.to_csv(output_file, index=False)
print(f"FX rate data saved to {output_file}")
