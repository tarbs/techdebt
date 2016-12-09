# create the base TechDebtReference table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtReference'

testdata = [
    {
        'ProductID': 'RDS::MySQL',
        'VersionID': '5.7.61',
        'InceptionDate': '20130101',
        'ExpectedEoLDate': '20170330',
        'ForcedUpgrade': True,
        'LastRecordedDatetime': '20161208085000',
        'Comments': 'This is a classic'
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

for item in testdata:
    returnval = table.put_item(
        Item=item,
        ReturnValues='ALL_OLD'
    )
    print(returnval)


print(table.item_count)
