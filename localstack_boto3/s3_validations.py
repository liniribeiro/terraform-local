import boto3


client = boto3.client('s3', endpoint_url="http://localhost:4566")
response = client.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')