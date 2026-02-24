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









