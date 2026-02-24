## Customer-Churn Analysis Project
## Author: Mandela Pulei

# Loading Necessary libraries

import pandas as pd
import numpy as np

client_df= pd.read_csv("client_data.csv")
price_df= pd.read_csv("price_data.csv")
print(client_df.head())
print(client_df.describe())

# Replace the text "MISSING" with actual null values (NaN)
client_df.replace("MISSING", np.nan, inplace=True)

print("\n--- Missing Values Count (After fixing 'MISSING' text) ---")
print("\n--- Missing Values in price_df ---")
print(client_df.isnull().sum())
print(price_df.isnull().sum())

# Convert date columns to datetime objects
client_df['date_activ'] = pd.to_datetime(client_df['date_activ'])
price_df['price_date'] = pd.to_datetime(price_df['price_date'])

# Verify the change
print("\n--- New Data Types for Dates ---")
print(f"Client date_activ type: {client_df['date_activ'].dtype}")
print(f"Price price_date type: {price_df['price_date'].dtype}")

# 1. Fill channel_sales with the most frequent value (Mode)
channel_mode = client_df['channel_sales'].mode()[0]
client_df['channel_sales'] = client_df['channel_sales'].fillna(channel_mode)

# 2. Fill origin_up with the most frequent value (Mode)
origin_mode = client_df['origin_up'].mode()[0]
client_df['origin_up'] = client_df['origin_up'].fillna(origin_mode)

# 3. Final Check: Everything should be 0 now
print("\n--- Final Null Check ---")
print(client_df.isnull().sum())

# Merge two datasets on the "id" columns
merged_df = pd.merge(client_df, price_df, on="id")

# Check the status of the merged_df
print("\n ---merged data shape ---")
print(f"Original Client Rows: {len(client_df)}")
print(f"New Merged Rows: {len(merged_df)}")

# Preview the combined Data
print(merged_df.head())

# Calculating the price difference for each customer
price_diff = merged_df.groupby("id").agg({"price_off_peak_var":["mean", "min", "max"],"churn":"mean"}).reset_index()
# Structure the column names
price_diff.columns = ["id", "off_peak_mean", "off_peak_min", "off_peak_max", "churn"]

# Feature Engineering
price_diff["price_spread"]= price_diff["off_peak_max"] - price_diff["off_peak_min"]

print("\n--- price_spread feature---")
print(price_diff.head())

# Groupby churn to see the average price_spread
churn_analysis = price_diff.groupby("churn")["price_spread"].mean()
print("\n--- average price spread by churn status---")
print(churn_analysis)

# Price Sensitivity
churn_analysis = price_diff.groupby('churn')['price_spread'].mean()
print("\n--- Summary: Average Price Spread by Churn Status ---")
print(churn_analysis)

price_diff.to_csv("processed_price_data.csv", index=False)
print("\nSuccess: Processed data saved to 'processed_price_data.csv'")











