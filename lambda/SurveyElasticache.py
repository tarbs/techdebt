
# Survey the current AWS account for running Elasticache clusters and log the details into DynamoDB

import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
from datetime import datetime


def lambda_handler(event, context):

    # Set up reference values
    tablename = 'TechDebtInstance'
    dateFormat = "%Y%m%d%H%M%S"
    dateStamp = datetime.utcnow().strftime(dateFormat)
    baseProductName = 'Elasticache::'
    productName = ''

    # Connect to AWS account via boto
    elasticache = boto3.client('elasticache')
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(tablename)
    clusters = elasticache.describe_cache_clusters()

    # extract the instance details and write to the table 

    for instance in clusters['CacheClusters']:

        productName = baseProductName + instance['Engine']
        instanceItem = {
            'ProductID': productName,
            'InstanceID': instance['CacheClusterId'],
            'VersionID': instance['EngineVersion'],
            'LastRecordedDatetime': dateStamp
        }
        # print(json.dumps(instanceItem))

        print('Adding ' + productName + '::' + instance['CacheClusterId'] )

        returnval = table.put_item(
            Item=instanceItem
        )


    # Find all Elasticache instances that were not modified today

    instancesToDelete = table.scan(
        ProjectionExpression="ProductID, InstanceID",
        FilterExpression='LastRecordedDatetime < :ts and begins_with(ProductID, :bPN)',
        ExpressionAttributeValues={
            ":ts": dateStamp,
            ":bPN": baseProductName
        }
    )

#    print(json.dumps(instancesToDelete,indent=4))

    for instance in instancesToDelete['Items']:

        print('Deleting ' + instance['ProductID'] + '::' + instance['InstanceID'])
        table.delete_item(
            Key={
                'ProductID': instance['ProductID'],
                'InstanceID': instance['InstanceID']
            }
        )

# TODO
#

# Survey db clusters  - for Aurora

# For local test execution
lambda_handler(0,0)
