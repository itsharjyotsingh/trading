import openpyxl

# Create a new workbook object
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Set the name of the worksheet
worksheet.title = "Sheet1"
workbook.save("example.xlsx")