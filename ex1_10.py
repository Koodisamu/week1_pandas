import pandas as pd

# data for random people
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 28, 35, 70]
}

df = pd.DataFrame(data1)

unique_categories = df['Age'].unique()

print(unique_categories)