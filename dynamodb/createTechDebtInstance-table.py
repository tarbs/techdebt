# create the base TechDebtInstance table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtInstance'

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName=tablename,
    KeySchema=[
        {
            'AttributeName': 'ProductID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'InstanceID',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ProductID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'InstanceID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

print(table.item_count)
