import pandas as pd
import os
import requests, zipfile, io

# 1️⃣ Set up folders (relative to this script's location)
raw_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")
os.makedirs(raw_folder, exist_ok=True)
output_file = os.path.join(raw_folder, "inflation.csv")

# 2️⃣ Download World Bank ZIP
url = "http://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=csv"
response = requests.get(url)
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # Find the CSV inside the ZIP (skip metadata CSV)
    csv_filename = [f for f in z.namelist() if f.endswith('.csv') and 'Metadata' not in f][0]
    with z.open(csv_filename) as f:
        df = pd.read_csv(f, skiprows=4)

# 3️⃣ Filter for Kenya
kenya_df = df[df['Country Name'] == 'Kenya']

# 4️⃣ Keep only columns that are actual years (4-digit)
year_cols = [c for c in kenya_df.columns if c.isdigit()]
kenya_df = kenya_df.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    value_vars=year_cols,
    var_name='year',
    value_name='inflation_rate'
)

# 5️⃣ Clean and sort
kenya_df = kenya_df[['year', 'inflation_rate']].sort_values('year')
kenya_df['year'] = kenya_df['year'].astype(int)

# 6️⃣ Save
kenya_df.to_csv(output_file, index=False)
print(f"Inflation data saved to {output_file}")
