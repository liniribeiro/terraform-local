import json

import boto3

client = boto3.client('secretsmanager', endpoint_url="http://localhost:4566", region_name="us-east-1")


secret = '{"host": "localhost", "username": "postgres", "password": "postgrespw",' \
         ' "dbname": "dbname", "port": "5432" }'

response = client.put_secret_value(
    SecretId='MyTestDatabaseSecret',
    SecretString=secret,
)


secret_name = f'MyTestDatabaseSecret'
get_secret_value_response = client.get_secret_value(
    SecretId=secret_name
)
secrets = json.loads(get_secret_value_response['SecretString'])
print(secrets)
