import requests

# Set the headers for the request
headers = {'Authorization': 'Bearer abc123'}

# Set the query parameters for the request
params = {'page': 2, 'per_page': 100}

# Send the GET request to the API endpoint
response = requests.get('https://api.example.com/endpoint', headers=headers, params=params)

# Check the status code of the response
if response.status_code == 200:
  # Read the response data
  data = response.json()
  # Do something with the data
  print(data)
else:
  # There was an error with the request
  print('Error:', response.status_code)
