# create the base TechDebtInstance table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtInstance'

testdata = [
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-1','VersionID': '5.7.61','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-2','VersionID': '5.7.61','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-3','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-4','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-5','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-6','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-7','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-8','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-9','VersionID': '5.5.40a','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-10','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-11','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-12','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-13','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-14','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-15','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-16','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-17','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-18','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-19','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-10','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::MySQL','InstanceID': 'andytest-MySQL-instance-21','VersionID': '5.6.27','LastRecordedDatetime': '20161208085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-1','VersionID': '9.6.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-2','VersionID': '9.6.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-3','VersionID': '9.6.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-4','VersionID': '9.3.9','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-5','VersionID': '9.3.9','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-6','VersionID': '9.3.9','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-7','VersionID': '9.3.9','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-8','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-9','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-10','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-11','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-12','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-13','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-14','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::PostgreSQL','InstanceID': 'andytest-PostgreSQL-instance-15','VersionID': '9.3.1','LastRecordedDatetime': '20161207085000'},
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