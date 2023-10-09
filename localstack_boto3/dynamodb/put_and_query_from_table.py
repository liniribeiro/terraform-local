from typing import Dict

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")


def put_data(log: Dict):
    table = dynamodb.Table('log_table')
    response = table.put_item(
       Item=log
    )
    return response


response = put_data({"type": "load", "text": "LOG", "time": "2022-08-12T17:26:08.1989978"})
print(response)


def query_from():
    table = dynamodb.Table('log_table')
    response = table.query(KeyConditionExpression=Key('type').eq('load'))
    return response['Items']


movies = query_from()
for movie in movies:
    print(movie)
    print(len(movies))
