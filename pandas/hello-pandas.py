import pandas as pd

# Column name
first_column = "first_column"

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

# Add Column
print("")
print("Add Columns:")
df0["second_column"] = 0
df0["third_column"] = "empty"
print(df0)

# Query
data_two_column = {"a": [1, 1, 2], "b": ["hello", "world", "world"]}
df_two_column = pd.DataFrame(data_two_column)
print(df_two_column)
print(df_two_column[df_two_column.a == 1])
print(df_two_column[df_two_column.b == "world"])
print(df_two_column.query("a == 1 & b =='world'"))

# Save & Load
print("")
print("Save & Load:")
df_two_column.to_csv("data.csv", index_label="id")
df_loaded = pd.read_csv("data.csv", index_col="id")
print(df_loaded)
print(df_loaded[df_two_column.a == 1])
print(df_loaded[df_two_column.b == "world"])
print(df_loaded.query("a == 1 & b =='world'"))
