import pandas as pd

# Define PPAAC decay function
def ppaac_decay(x, t, lambda_val):
    return x * (1 - lambda_val)**t

# Load CSV file into a Pandas dataframe
df = pd.read_csv('OutputMAC000084.csv')

# Apply zero sum decay to each element
lambda_val = 0.5  # Set lambda value
for i in range(len(df)):
    for j in range(len(df.columns)):
        df.iloc[i, j] = ppaac_decay(df.iloc[i, j], i+j, lambda_val)

# Save modified dataframe to new CSV file
df.to_csv('PPAACMAC000084.csv', index=False)
