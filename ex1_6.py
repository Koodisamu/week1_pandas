import pandas as pd

# data for random people
data1 = {
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 18, 35, 29],
    'Score': [2, 6, 10, 1, 3]
}

data2 = {
    'Name': ['Hanna', 'Noora', 'Kaisa', 'Raisa', 'Maisa'],
    'Age': [17, 24, 56, 37, 29],
    'Occupation': ['Trainee', 'Product Manager', 'Sales Manager', 'Data Engineer', 'CEO']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(f"\n {df2}")

concatenated_df = pd.concat([df1, df2], ignore_index=True)

print(f"\n {concatenated_df}")