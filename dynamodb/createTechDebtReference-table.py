# create the base TechDebtReference table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtReference'

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName=tablename,
    KeySchema=[
        {
            'AttributeName': 'ProductID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'VersionID',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ProductID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'VersionID',
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
