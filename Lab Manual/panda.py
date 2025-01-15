# import pandas as pd

# # Step 1: Create a DataFrame
# data = {
#     'Name': ['Prashant', 'Shashank', 'Joe', 'Beck'],
#     'Age': [24, 27, 22, 32],
#     'Salary': [50000, 60000, 55000, 80000]
# }
# df = pd.DataFrame(data)

# # Step 2: Display the DataFrame
# print("DataFrame:")
# print(df)

# # Step 3: Perform Basic Aggregation Functions
# print("\nBasic Aggregation Results:")
# print(f"Mean Age: {df['Age'].mean()}")
# print(f"Total Salary: {df['Salary'].sum()}")
# print(f"Minimum Age: {df['Age'].min()}")
# print(f"Maximum Salary: {df['Salary'].max()}")
# print(f"Count of Rows: {df.shape[0]}")

# import pandas as pd

# # Create a DataFrame
# data = {
#     'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
#     'Salary': [50000, 60000, 55000, 52000, 62000, 54000, 58000, 61000, 57000],
#     'Experience': [2, 5, 3, 4, 6, 2, 3, 4, 3]
# }
# df = pd.DataFrame(data)

# # Group data by 'Department' and aggregate
# result = df.groupby('Department').agg({
#     'Salary': ['sum', 'mean'],
#     'Experience': 'mean'
# })

# # Display results
# print(result)

import matplotlib.pyplot as plt
# Sample data: Temperature variations over a week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [26, 20, 19, 27, 28, 25, 22] # Replace with actual temperatures if available
# Creating the line plot
plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue', linewidth=2)
# Adding titles and labels
plt.title('Temperature Variations Over a Week')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
# Displaying the temperature values on the plot
for i, temp in enumerate(temperatures):
 plt.text(i, temp + 0.5, f'{temp}°C', ha='center')
# Displaying the plot
plt.show()