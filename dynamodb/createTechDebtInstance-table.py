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
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-1','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-2','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-3','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-4','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-5','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-6','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-7','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-8','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-9','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-10','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-11','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-12','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-13','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-14','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-15','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-16','VersionID': '12.00.5000.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-17','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-18','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-19','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-20','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-21','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-22','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-23','VersionID': '12.00.4422.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-24','VersionID': '13.00.2164.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-25','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'RDS::SQLServer::Express','InstanceID': 'andytest-SQLExpress-instance-26','VersionID': '10.50.2789.0.v1','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-1','VersionID': '2.6.13','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-2','VersionID': '2.6.13','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-3','VersionID': '2.8.19','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-4','VersionID': '2.8.19','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-5','VersionID': '2.8.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-6','VersionID': '3.2.4','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-7','VersionID': '3.2.4','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-8','VersionID': '3.2.4','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Redis','InstanceID': 'andytest-ElasticacheRedis-instance-9','VersionID': '3.2.4','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-1','VersionID': '1.4.14','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-2','VersionID': '1.4.14','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-3','VersionID': '1.4.14','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-4','VersionID': '1.4.14','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-5','VersionID': '1.4.14','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-6','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-7','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-8','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-9','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-10','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-11','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-12','VersionID': '1.4.24','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-13','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-14','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-15','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-16','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-17','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-18','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-19','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-20','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-21','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-22','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-23','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-24','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-25','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-26','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-27','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-28','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticache::Memcached','InstanceID': 'andytest-ElasticacheMemcached-instance-29','VersionID': '1.4.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-1','VersionID': '1.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-2','VersionID': '1.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-3','VersionID': '1.5','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-4','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-5','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-6','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-7','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-8','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'Elasticsearch','InstanceID': 'andytest-Elasticsearch-instance-9','VersionID': '2.3','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-1','VersionID': 'emr-4.0.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-2','VersionID': 'emr-4.1.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-3','VersionID': 'emr-4.1.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-4','VersionID': 'emr-4.5.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-5','VersionID': 'emr-4.5.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-6','VersionID': 'emr-4.5.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-7','VersionID': 'emr-4.5.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-8','VersionID': 'emr-4.5.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-9','VersionID': 'emr-4.580','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-10','VersionID': 'emr-4.8.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-11','VersionID': 'emr-4.8.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-12','VersionID': 'emr-4.8.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-13','VersionID': 'emr-4.8.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-14','VersionID': 'emr-4.8.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-15','VersionID': 'emr-5.2.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-16','VersionID': 'emr-5.2.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-17','VersionID': 'emr-5.2.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-18','VersionID': 'emr-5.2.0','LastRecordedDatetime': '20161207085000'},
    {'ProductID': 'ElasticMapReduce::Amazon','InstanceID': 'andytest-EMR-instance-19','VersionID': 'emr-5.2.0','LastRecordedDatetime': '20161207085000'}
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