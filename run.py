import pandas as pd

# Read the Excel file
df = pd.read_excel('cse_schedule.xlsx', skiprows=5, nrows=451)  # skiprows=5 to start from row 6, nrows=451 to read till row 456

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Write JSON data to a file
with open('output.json', 'w') as f:
    f.write(json_data)
