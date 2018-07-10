from pandas.io.parsers import read_csv

customer_csv_file = 'DA_Customer.csv'

customer_dataframe = read_csv(customer_csv_file, delimiter=';')

# Print 6th Row
print(customer_dataframe.iloc[6])

# Print 6th Row and 0th Index of Column
print(customer_dataframe.iloc[6][0])

# Print Top 5 rows
print("\nTop 5 Rows are")
print(customer_dataframe.head(5))

# Print Last 5 Rows
print("\n Last 5 rows are")
print(customer_dataframe.tail(5))


# Group the data by City
city_group = customer_dataframe.groupby('City')
count = 0

for city_name, group in city_group:
    count = count + 1
    print("City", count, city_name)
    print(group)


