
import pandas as pd
import numpy as np
import os

# 1️⃣ Set up folders
raw_folder = "C:/Users/USER/OneDrive/Desktop/projects/macroguard/data/raw"
os.makedirs(raw_folder, exist_ok=True)
output_file = os.path.join(raw_folder, "interest.csv")

# 2️⃣ Define the time range based on your other datasets
# Example: inflation dataset from 2000 to 2025
start_year = 2000
end_year = 2025

dates = pd.date_range(start=f'{start_year}-01-01', end=f'{end_year}-12-01', freq='MS')

# 3️⃣ Simulate realistic interest rates
np.random.seed(42)  # for reproducibility
interest_rates = np.random.uniform(4, 12, len(dates))  # random rates between 4% and 12%

# 4️⃣ Build the DataFrame
df = pd.DataFrame({
    'date': dates,
    'interest_rate': interest_rates
})

# 5️⃣ Save to raw folder
df.to_csv(output_file, index=False)
print(f"Simulated interest rate data saved to {output_file}")
print(df.head())
print(f"Dataset has {len(df)} rows, matching other datasets.")
