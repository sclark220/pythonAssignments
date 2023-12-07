import pandas

# This is all commented out because I was printing as I went

# Create
dataFrame = pandas.read_csv('telco_churn.csv') # From csv

tempDictionary = {'row0':["numbers", "more numbers", "more numbers 2"], 'row1':[1,2,3], 'row2':[4,5,6], 'row3':[7,8,9]} 

dictionaryDataFrame = pandas.DataFrame.from_dict(tempDictionary, orient='index') # From Dictionary (I like rows better)


# Read
#print(dictionaryDataFrame.head())
#print(dataFrame.head(10)) # Top Rows

#print(dataFrame.tail(10)) # Bottom rows


# Columns and Data Type
#print(f"\nThese are the columns \n {dataFrame.columns} \nEnd of the Columns \n")

#print(f"\nThese are the types \n {dataFrame.dtypes} \nEnd of the types \n")


# Summary Statictics
#print(dataFrame.describe()) # This is pretty cool

#print(dataFrame.describe(include='object'))


# Filtering Columns
#print(dataFrame.State)

#print(dataFrame['International plan'])

#print(dataFrame[['State', 'International plan']])

#print(dataFrame.Churn.unique())


# Filtering Rows
#print(dataFrame[dataFrame['International plan']=='No'])

#print(dataFrame[(dataFrame['International plan']=='No') & (dataFrame['Churn']==True)])


# Indexing with iloc
#print(dictionaryDataFrame.iloc[0])

#print(dataFrame.iloc[14])

#print(dataFrame.iloc[14,-1])

#print(dataFrame.iloc[22:33])


# Indexing wiht Ioc
#state = dataFrame.copy()

#state.set_index('State', inplace=True)

#print(state.head())

#print(state.loc['OH'])


# Update
# Dropping Rows
#print(dataFrame.isnull().sum())

#dataFrame.dropna(inplace=True)

#print(dataFrame.isnull().sum())


# Dropping Columns
#print(dataFrame.drop('Area code', axis=1))


# Creating Calculated Columns
#dataFrame['New Column'] = dataFrame['Total night minutes'] + dataFrame['Total intl minutes']
#print(dataFrame.head())


# Update entire Column
#dataFrame['New Column'] = 100
#print(dataFrame.head())


# Up dating a single value
#dataFrame.iloc[0,-1] = 10
#print(dataFrame.head())


# Condiition based updating using apply
#dataFrame['Churn Binary'] = dataFrame['Churn'].apply(lambda x: 1 if x==True else 0)
#print(dataFrame[dataFrame['Churn']==True].head())


# Output to CSV
dataFrame.to_csv('output.csv')


#Output to JSON
#df.to_json()


# Delete a data frame
#del dataFrame