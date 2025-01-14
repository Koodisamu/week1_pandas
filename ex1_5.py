import pandas as pd

# data for random people
data = {
    'Name': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
    'Age': [28, 70, 18, 35, 29],
    'Score': [2,None, 10, None, 3]
}

df = pd.DataFrame(data)

df['Score'] = df['Score'].astype(float)

print(df)

df_filled = df.fillna({'Score': df['Score'].mean()})

print(df_filled)