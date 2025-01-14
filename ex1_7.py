import pandas as pd

# data for random people
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 18, 35, 29]
}

data2 = {
    'ID': [1, 2, 3, 4, 5],
    'Occupation': ['Trainee', 'Product Manager', 'Sales Manager', 'Data Engineer', 'CEO'],
    'Salary': [2500, 5500, 4900, 10000, 9500]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='ID', how='inner')

print(f" \n{merged_df}")