# create the base TechDebtInstance table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtInstance'

testdata = [
    {
        'ProductID': 'RDS::MySQL',
        'InstanceID': 'andytest-MySQL-instance-1',
        'VersionID': '5.7.61',
        'LastRecordedDatetime': '20161208085000'
    }
]

dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table(tablename)

if table is None:
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

for item in testdata:
    returnval = table.put_item(
        Item=item,
        ReturnValues='ALL_OLD'
    )
    print(returnval)


print(table.item_count)