import pandas as pd

# data for random people
data = {
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 18, 35, 29],
    'Score': [2, 6, 10, 1, 3]
}

df = pd.DataFrame(data)
print(df)

df['Score'] = df['Score'].astype(float)

print(df)