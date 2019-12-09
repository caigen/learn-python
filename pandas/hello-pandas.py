import pandas as pd

# Column name
first_column = "first column"

# No data
data0 = {first_column: []}
df0 = pd.DataFrame(data0)

# Data
data1 = {first_column: [101, 102]}
df1 = pd.DataFrame(data1)

data2 = {first_column: [201, 202]}
df2 = pd.DataFrame(data2)

print(df0)
print(df1)
print(df2)

# Change
df0 = df1.append(df2, ignore_index=True)
print(df1)
print(df2)
print(df0)
