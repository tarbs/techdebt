import boto3
import json

def lambda_handler(event, context):

    testdata = [
        'a': 'aaa',
        'b': 'bbb',
        'c': 'ccc',
        'd': 'ddd'
    ]