# create the base TechDebtReference table in dynamodb
#
# Uses the local AWS configuration for account access

import boto3

tablename = 'TechDebtReference'

testdata = [
    {'ProductID': 'RDS::mysql','VersionID': '5.5.40a','InceptionDate': '20120101','ExpectedEoLDate': '20150330','ForcedUpgrade': True,'Comments': "Ooooh, that's old"},
    {'ProductID': 'RDS::mysql','VersionID': '5.6.16','InceptionDate': '20140101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': "so so"},
    {'ProductID': 'RDS::mysql','VersionID': '5.6.27','InceptionDate': '20140101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': "A classic"},
    {'ProductID': 'RDS::mysql','VersionID': '5.7.61','InceptionDate': '20150101','ExpectedEoLDate': '20160623','ForcedUpgrade': True,'Comments': 'The best'},
    {'ProductID': 'RDS::postgresql','VersionID': '9.6.1','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'RDS::postgresql','VersionID': '9.3.9','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'RDS::postgresql','VersionID': '9.3.1','InceptionDate': '20130101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '10.50.2789.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '12.00.4422.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'RDS::SQLServer::Express','VersionID': '12.00.5000.0.v1','InceptionDate': '20100101','ExpectedEoLDate': '20140330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Redis','VersionID': '2.6.13','InceptionDate': '20100101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Redis','VersionID': '2.8.19','InceptionDate': '20150101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Redis','VersionID': '2.8.24','InceptionDate': '20140101','ExpectedEoLDate': '20170930','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Redis','VersionID': '3.2.4','InceptionDate': '20140101','ExpectedEoLDate': '20170930','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Memcached','VersionID': '1.4.14','InceptionDate': '20160101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Memcached','VersionID': '1.4.24','InceptionDate': '20160101','ExpectedEoLDate': '20180330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticache::Memcached','VersionID': '1.4.5','InceptionDate': '20160101','ExpectedEoLDate': '20190330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticsearch','VersionID': '1.5','InceptionDate': '20150101','ExpectedEoLDate': '20170330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'Elasticsearch','VersionID': '2.3','InceptionDate': '20160101','ExpectedEoLDate': '20190330','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'ElasticMapReduce::Amazon','VersionID': 'emr-4.0.0','InceptionDate': '20120101','ExpectedEoLDate': '20170130','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'ElasticMapReduce::Amazon','VersionID': 'emr-4.1.0','InceptionDate': '20120101','ExpectedEoLDate': '20170130','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'ElasticMapReduce::Amazon','VersionID': 'emr-4.5.0','InceptionDate': '20120101','ExpectedEoLDate': '20170130','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'ElasticMapReduce::Amazon','VersionID': 'emr-4.8.0','InceptionDate': '20120101','ExpectedEoLDate': '20170130','ForcedUpgrade': True,'Comments': " "},
    {'ProductID': 'ElasticMapReduce::Amazon','VersionID': 'emr-5.2.0','InceptionDate': '20120101','ExpectedEoLDate': '20170130','ForcedUpgrade': True,'Comments': " "}
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
