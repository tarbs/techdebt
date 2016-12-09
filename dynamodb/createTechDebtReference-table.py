# create the base TechDebtReference table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtReference'

testdata = [
    {'ProductID': 'RDS::MySQL','VersionID': '5.7.61','InceptionDate': '20150101','ExpectedEoLDate': '20160623','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': 'The best'},
    {'ProductID': 'RDS::MySQL','VersionID': '5.5.40a','InceptionDate': '20120101','ExpectedEoLDate': '20150330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': "Ooooh, that's old"},
    {'ProductID': 'RDS::MySQL','VersionID': '5.6.27','InceptionDate': '20140101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': "A classic"},
    {'ProductID': 'RDS::PostgreSQL','VersionID': '9.6.1','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::PostgreSQL','VersionID': '9.3.9','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::PostgreSQL','VersionID': '9.3.1','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '10.50.2789.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '12.00.4422.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '12.00.5000.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '13.00.2164.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'LastRecordedDatetime': '20161208085000','Comments': " "}
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
