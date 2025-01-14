import pandas as pd

# dates and birthdays
data1 = {
    'Date': ['1997-12-27', '1967-06-08', '1980-09-20', '2000-12-01', '1975-04-14'],
    'Birthday': ['Kalle', 'Ville', 'Jukka', 'Seppo', 'Kari'],
}

df = pd.DataFrame(data1)

df['Date'] = pd.to_datetime(df['Date'])

print(df)

df.rename(columns={'Date': 'EventDate', 'Birthday': 'EventValue'}, inplace=True)

print()
print(df)
