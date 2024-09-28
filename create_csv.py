import csv

# Sample data
data = [
    ["name", "age", "grade"],
    ["Archana", 18, 85.5],
    ["Baru", 20, 90.0],
    ["Raru", 17, 78.0],
    ["Divya", 21, 92.5]
]

# Write to CSV file
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")



OUTPUT:
CSV file created successfully.