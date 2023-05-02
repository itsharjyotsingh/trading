import openpyxl

# Create a new workbook object
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Write some data to the worksheet
worksheet['A1'] = 'Hello'
worksheet['B1'] = 'world!'

# Save the workbook to a file
workbook.save('example.xlsx')
