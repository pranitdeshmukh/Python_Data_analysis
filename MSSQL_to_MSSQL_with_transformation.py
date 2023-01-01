import pyodbc
import datetime

# Connect to the database
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=server_name;'
                      'DATABASE=database_name;'
                      'UID=username;'
                      'PWD=password')

# Create a cursor
cursor = cnxn.cursor()

# Execute a SELECT statement to retrieve the data
cursor.execute("SELECT * FROM table_name")

# Iterate through the rows and change the format of the date column
for row in cursor:
    date_column = row[1]  # Assume the date column is the second column in the table
    new_date_format = datetime.datetime.strftime(date_column, '%Y-%m-%d')
    # Update the row with the new date format
    cursor.execute("UPDATE table_name SET date_column = ? WHERE id = ?", (new_date_format, row[0]))

# Commit the changes to the database
cnxn.commit()

# Close the cursor and connection
cursor.close()
cnxn.close()
