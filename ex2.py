import pandas as pd

#ex2_1, Download titanic dataset from the link below and drag it to your exercise folder:
file_path = 'titanic.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

#ex2_2, Rename columns not to have any whitespaces or special characters.
df.columns = df.columns.str.strip().str.replace(' ', '').str.replace('/', '')

#ex2_3, For all person under the age of 18, set "sex" column value to be "child“.
df.loc[df['Age'] < 18, 'Sex'] = 'child'

#ex2_4, Create a new dataset which displays the average fare per sex.
avgfare4 = df.groupby('Sex')['Fare'].mean().reset_index()
avgfare4.columns = ['Sex', 'Avgfare']
#print(avgfare4)

#ex2_5, Create a new dataset which displays the average fare per sex and Pclass
avgfare5 = df.groupby(['Sex', 'Pclass'])['Fare'].mean().reset_index()
avgfare5.columns = ['Sex', 'Pclass', 'Avgfare']
#print(avgfare5)

#ex2_6, Create a new dataset which displays the average fare per survived column
avgfare6 = df.groupby('Survived')['Fare'].mean().reset_index()
avgfare6.columns = ['Survived', 'Avgfare']
#print(avgfare6)

#ex2_7, Split the dataset into 3 datasets based on the sex column. So one for male, another for female and third for child.
#       How many records does each dataset have?
male_df = df[df['Sex'] == 'male']
female_df = df[df['Sex'] == 'female']
child_df = df[df['Sex'] == 'child']

male_df_size = male_df.shape
female_df_size = female_df.shape
child_df_size = child_df.shape

print(f"Male records: {male_df_size[0]}, Female records: {female_df_size[0]}, Child records: {child_df_size[0]}")

#ex2_8, Create a new dataset that only includes Pclass, Name and age,
#       for those persons that had siblings, spouces, parents or children aboard.

dfex8_1 = df[(df['SiblingsSpousesAboard'] > 0) | (df['ParentsChildrenAboard'] > 0)]
dfex8_2 = dfex8_1[['Pclass', 'Name', 'Age']]
# print(dfex8.head(20))
# print(dfex8.shape)

#ex2_9, Filter off those persons who had both siblings/spouces AND parents/children.
dfex9_1 = dfex8_1[(dfex8_1['SiblingsSpousesAboard'] > 0) ^ (dfex8_1['ParentsChildrenAboard'] > 0)]

#dfex9_2 = dfex9_1[['SiblingsSpousesAboard', 'Name', 'ParentsChildrenAboard']]
#print(dfex9_2.head(20))

#ex2_10, What is the average fare paid by the people in the dataset from last step?
avgfare10 = dfex9_1['Fare'].mean()
print(f"Average fare paid by the people in the dataset from last step: {avgfare10}")
#print(df.columns)