import boto3

# Connect to the S3 service using your access key and secret key
s3 = boto3.client('s3',
                  aws_access_key_id='your_access_key',
                  aws_secret_access_key='your_secret_key')

# Specify the bucket and file you want to read
bucket_name = 'my-bucket'
file_name = 'data.csv'

# Read the file into memory
response = s3.get_object(Bucket=bucket_name, Key=file_name)
file_content = response['Body'].read()

# Print the file content
print(file_content)



#Using Pandas library


import pandas as pd

# Specify the URL of the file in the S3 bucket
s3_url = 's3://my-bucket/data.csv'

# Read the file into a DataFrame, passing in your access key and secret key
df = pd.read_csv(s3_url, key='your_access_key', secret='your_secret_key')

# Print the DataFrame
print(df)
