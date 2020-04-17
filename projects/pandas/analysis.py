import pandas as pd

### ways of reading different types of files
df = pd.read_csv('../../pandas-master/pokemon_data.csv')
df_xlsx = pd.read_excel('../../pandas-master/pokemon_data.xlsx')
df_txt = pd.read_csv('../../pandas-master/pokemon_data.txt', delimiter='\t')


### show only 5 rows
# print(df_txt.head(3))


### read headers
# print(df.columns)


### read each column
# print(df['Name'][0:5])
# print(df.Name[0:5])
# print(df[['Name', 'HP']])


### read each row
# print(df.iloc[0:5])

# for index, row in df.iterrows():	## helps reformat view
	# print(index, row['Name'])
	# print(index, row)

#print(df.loc[df['Type 1']== 'Fire'])	## with some conditions


### some stat.info abot data
# print(df.describe())


### sorting
# print(df.sort_values(['Name', 'HP'], ascending=False))
# print(df.sort_values(['Name', 'HP'], ascending=[0,1]))	##the same


### read a srecific location (R,C)
# print(df.iloc[2,1]) #[row, column]


### making changes to the data
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df = df.drop(columns=['Total'])	## deleting the column

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)	## another way of sum

# cols = list(df.columns.values)	## variable with list of columns to shorter inserting line
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]	## inserting column in the "middle"


### saving to files
# df.to_csv('modified.csv', index=False)	## save to csv
# df.to_excel('modified.xlsx', index=False)	## save to excel
# df.to_csv('modified.txt', index=False, sep='\t')	## save to txt


### filtering data
# df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]	## cond1 and cond2
# new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]	## cond1 OR cond2

# new_df = new_df.reset_index()	## reseting old index with new quatity of data. it is adding new column with old index
# new_df = new_df.reset_index(drop=True)	## reseting old index without column 'old index'

# new_df = df.loc[df['Name'].str.contains('Mega')]	## filter all data that contains smth
# new_df = df.loc[~df['Name'].str.contains('Mega')]	## all data that doen't contain smth

import re	## importing regular expressions
df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]	## contains cond1 or cond2, flags for ignoring the register

# print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])	## filtering data that starts with 'pi'. ^ means that it starts with smth, [a-z]* means that all letters contain

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'	## change smth on smth else
df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'	## change it back
df.loc[df['Type 1'] == 'Grass', 'Speed'] = 500	## also we can change another field based on this filter

df = pd.read_csv('modified.csv')


### conditional changes
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST'	## change both columns with one value
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST', 'TEST 2']	## change both columns with diff values


### aggregate statistics
# df = df.groupby(['Type 1']).mean()	## group by type 1 with average values
# df = df.groupby(['Type 1']).mean().sort_values('HP', ascending=True)	## sort the values
# df = df.groupby(['Type 1']).sum()	## group by type 1 with sum of values
# df = df.groupby(['Type 1']).count()	## counts by type 1
# df['count'] = 1
# df.groupby(['Type 1', 'Type 2']).count()['count']	## shows only one column with count and sort by type 1 and then by type 2


## working with large amount of data
# for df in pd.read_csv('modified.csv', chunksize=5):	## spliting on chunks with 5 rows
# 	print('Chunks')
# 	print(df)


new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
	results = df.groupby(['Type 1']).count()
	new_df = pd.concat([new_df, results])	## count data by chunks

print(new_df)



# print(df)

# print(df)
# print(new_df)
