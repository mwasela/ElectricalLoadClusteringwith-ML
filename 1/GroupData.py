import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file
data = pd.read_csv('lcl-june2015v2_2.csv')
data['DateTime'] = pd.to_datetime(data['DateTime']) # convert to datetime
# Set the date range for the 30-day period
end_date = datetime(2013, 12, 20)
start_date = end_date - timedelta(days=223)


for i in range(69, 101):
    user_id = f"MAC000{i:03d}"
    user_data = data[(data['LCLid'] == user_id) & (data['DateTime'] >= start_date) & (data['DateTime'] < end_date)]

    # Add a new column for the date only
    user_data['Date'] = user_data['DateTime'].dt.date

    # Calculate the daily usage for each day
    daily_data = user_data.groupby('Date')['KWH'].sum().to_frame('sum')
   

    # Save the daily data to a CSV file
    daily_data.to_csv(f'{user_id}.csv', sep=',')

