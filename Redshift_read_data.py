import psycopg2

# Connect to the database
conn = psycopg2.connect(host="host_name",
                        port=5439,
                        database="database_name",
                        user="username",
                        password="password")

# Create a cursor
cur = conn.cursor()

# Execute a SELECT statement to retrieve the data
cur.execute("SELECT * FROM table_name")

# Fetch the rows from the cursor
rows = cur.fetchall()

# Iterate through the rows and print the data
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()


#Reading data using pandas


import pandas as pd
import psycopg2

# Connect to the database
conn = psycopg2.connect(host="host_name",
                        port=5439,
                        database="database_name",
                        user="username",
                        password="password")

# Use the read_sql() function to read the data into a DataFrame
df = pd.read_sql("SELECT * FROM table_name", conn)

# Print the DataFrame
print(df)

# Close the connection
conn.close()
