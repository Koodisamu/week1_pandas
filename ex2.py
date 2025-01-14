import pandas as pd

# data for random people
data = {
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 18, 35, 29],
    'Score': [2, 6, 10, 1, 3]
}

df = pd.DataFrame(data)

df_index = df.set_index('Name')
print(df_index)

filtered_df = df_index[df_index['Age'] > 25]

print(filtered_df)