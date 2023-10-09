import boto3


client = boto3.client('dynamodb', endpoint_url="http://localhost:4566")

response = client.list_tables()
print(response)