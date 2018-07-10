from pandas.io.parsers import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')


customer_csv = 'DA_Customer.csv'
customer_call_details = 'DA_Call_Details.csv'

customer_dataframe = read_csv(customer_csv, dtype=dict(Customer_ID=str))


customer_call_details_dataframe = read_csv(customer_call_details, dtype=dict(Customer_ID=str))

# Assign Results to New DataFrame
result_dataframe = pd.merge(customer_dataframe, customer_call_details_dataframe, on='Customer_ID')

result_dataframe.to_csv('DA_Final.csv')

# Group the DataFrame by City
customer_city_group = result_dataframe.groupby('City')

# Retrieve City Names from City Group
city_name = customer_city_group.groups.keys()

# Count the Number of Customers Per City
customer_count_per_city = customer_city_group['Customer_ID'].nunique()

print(city_name)
print(customer_count_per_city)


# Set the Graph Settings
customer_count_per_city.plot(kind='bar', title='Customer Demographics', figsize=(10, 20))

# Set X Axis Label
plt.xlabel('City')

# Set Y Axis Label
plt.ylabel('Number of Customers')

# Plot the Graph on Screen
#plt.show()

# City with Largest Customer base
print("City with the Largest Customer Base", customer_count_per_city.idxmax())
print("Highest Number of Subscribers in the City", customer_count_per_city.idxmax(), "are",
      customer_count_per_city.max())

# City Talks a lot
city_call_duration = customer_city_group['Call Duration'].sum()

print("City Call Duration in Seconds")
print(city_call_duration)
print(city_call_duration.idxmax(), city_call_duration.max())

print("Average Call Duration of All Customers")
print(int(city_call_duration.mean()))

# Call Duration Per Customer Yearly
result_dataframe['Calling Date'] = pd.to_datetime(result_dataframe['Calling Date'])
customer_call_duration = result_dataframe.groupby([result_dataframe['Calling Date'].dt.year, 'Customer_ID'])

print(customer_call_duration.groups.keys())

print(customer_call_duration['Call Duration'].sum())








