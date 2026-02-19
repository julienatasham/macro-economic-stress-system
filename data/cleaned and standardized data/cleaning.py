import pandas as pd
import os

# 1️⃣ Paths
raw_folder = "C:/Users/USER/OneDrive/Desktop/projects/macroguard/data/raw"
processed_folder = "C:/Users/USER/OneDrive/Desktop/projects/macroguard/data/cleaned and standardized data"
os.makedirs(processed_folder, exist_ok=True)
output_file = os.path.join(processed_folder, "macro_data.csv")

# 2️⃣ Load datasets
inflation = pd.read_csv(os.path.join(raw_folder, "inflation.csv"))
fx = pd.read_csv(os.path.join(raw_folder, "fx.csv"))  # or your tempfx.csv
interest = pd.read_csv(os.path.join(raw_folder, "interest.csv"))
fuel = pd.read_csv(os.path.join(raw_folder, "fuelprice.csv"))

# 3️⃣ Standardize column names
inflation = inflation.rename(columns={"year": "date", "inflation_rate": "inflation_rate"})
inflation['date'] = pd.to_datetime(inflation['date'], format='%Y')

fx = fx.rename(columns={"Date": "date", "fx_kes_usd": "fx_kes_usd"})
fx['date'] = pd.to_datetime(fx['date'])

interest = interest.rename(columns={"Date": "date", "Rate": "interest_rate"})
interest['date'] = pd.to_datetime(interest['date'])

fuel = fuel.rename(columns={"Date": "date", "Price_USD": "fuel_price_usd"})
fuel['date'] = pd.to_datetime(fuel['date'])

# 4️⃣ Make inflation monthly (repeat yearly value for all months)
inflation_monthly = inflation.copy()
inflation_monthly = inflation_monthly.set_index('date').resample('M').ffill().reset_index()

# 5️⃣ Merge datasets
# Start with FX as base (assuming daily/monthly data)
master = fx.copy()
master = master.merge(interest, on='date', how='left')
master = master.merge(fuel, on='date', how='left')
master = master.merge(inflation_monthly, on='date', how='left')

# 6️⃣ Sort by date
master = master.sort_values('date').reset_index(drop=True)

# 7️⃣ Save
master.to_csv(output_file, index=False)
print(f"Master dataset saved to {output_file}")
