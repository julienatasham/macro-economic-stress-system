# eda_macro_combined.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# 1. Load data
# ---------------------------
data_path = r"C:\Users\USER\OneDrive\Desktop\projects\macroguard\data\cleaned and standardized data\macro_data.csv"
df = pd.read_csv(data_path)

# ---------------------------
# 2. Convert columns to correct types
# ---------------------------
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['fx_kes_usd'] = pd.to_numeric(df['fx_kes_usd'], errors='coerce')
df['interest_rate'] = pd.to_numeric(df['interest_rate'], errors='coerce')
df['fuel_price_usd'] = pd.to_numeric(df['fuel_price_usd'], errors='coerce')
df['inflation_rate'] = pd.to_numeric(df['inflation_rate'], errors='coerce')

# ---------------------------
# 3. Summary stats
# ---------------------------
print(df.info())
print(df.describe())

# ---------------------------
# 4. Create output folder for plots
# ---------------------------
plot_dir = r"C:\Users\USER\OneDrive\Desktop\projects\macroguard\eda_plots"
os.makedirs(plot_dir, exist_ok=True)

# ---------------------------
# 5. Line plots over time
# ---------------------------
features = ['fx_kes_usd', 'interest_rate', 'fuel_price_usd', 'inflation_rate']
colors = ['#FF69B4', '#9370DB', '#1f77b4', '#ff7f0e']  # pink, purple, blue, orange

for feature, color in zip(features, colors):
    plt.figure(figsize=(14,6))
    plt.plot(df['date'], df[feature], color=color, linewidth=2)
    plt.title(f"{feature} over time", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel(feature)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    save_path = os.path.join(plot_dir, f"{feature}_over_time.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot: {save_path}")

# ---------------------------
# 6. Histograms
# ---------------------------
for feature, color in zip(features, colors):
    plt.figure(figsize=(10,5))
    sns.histplot(df[feature], kde=True, color=color, bins=30)
    plt.title(f"Distribution of {feature}", fontsize=16)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.tight_layout()
    save_path = os.path.join(plot_dir, f"{feature}_histogram.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot: {save_path}")

# ---------------------------
# 7. Boxplots
# ---------------------------
for feature, color in zip(features, colors):
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df[feature], color=color)
    plt.title(f"Boxplot of {feature}", fontsize=16)
    plt.tight_layout()
    save_path = os.path.join(plot_dir, f"{feature}_boxplot.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot: {save_path}")

# ---------------------------
# 8. Correlation heatmap
# ---------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[features].corr(), annot=True, fmt=".2f", cmap="PuRd", linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=16)
plt.tight_layout()
save_path = os.path.join(plot_dir, "correlation_heatmap.png")
plt.savefig(save_path)
plt.close()
print(f"Saved plot: {save_path}")

print("EDA complete. All plots saved to:", plot_dir)
