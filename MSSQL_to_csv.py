import pyodbc
import csv


# Connect to the database
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=server_name;'
                      'DATABASE=database_name;'
                      'UID=username;'
                      'PWD=password')

# Create a cursor
cursor = cnxn.cursor()

# Execute a SELECT statement
cursor.execute("SELECT * FROM table_name")

# Iterate through the rows of the result set
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
cnxn.close()




# Connect to the database (as shown in the previous example)

# Create a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the column names
    writer.writerow([column[0] for column in cursor.description])

    # Write the rows
    writer.writerows(cursor)
