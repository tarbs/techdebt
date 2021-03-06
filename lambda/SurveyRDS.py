
# Survey the current AWS account for running RDS instances and log the details into DynamoDB

import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
from datetime import datetime


def lambda_handler(event, context):

    # Set up reference values
    tablename = 'TechDebtInstance'
    dateFormat = "%Y%m%d%H%M%S"
    dateStamp = datetime.utcnow().strftime(dateFormat)

    # Connect to AWS account via boto
    rds = boto3.client('rds')
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(tablename)
    rdsInstances = rds.describe_db_instances()

    # extract the instance details and write to the table 

    for instance in rdsInstances['DBInstances']:

        productName = 'RDS::' + instance['Engine']
        instanceItem = {
            'ProductID': productName,
            'InstanceID': instance['DBInstanceIdentifier'],
            'VersionID': instance['EngineVersion'],
            'LastRecordedDatetime': dateStamp
        }
        # print(json.dumps(instanceItem))

        print('Adding ' + productName + '::' + instance['DBInstanceIdentifier'] )

        returnval = table.put_item(
            Item=instanceItem
        )


    # Find all RDS instances that were not modified today


    instancesToDelete = table.scan(
        ProjectionExpression="ProductID, InstanceID",
        FilterExpression='LastRecordedDatetime < :ts and begins_with(ProductID, :bPN)',
        ExpressionAttributeValues={
            ":ts": dateStamp,
            ":bPN": baseProductName
        }
    )


    for instance in instancesToDelete['Items']:

        print('Deleting ' + productName + '::' + instance['InstanceID'])
        table.delete_item(
            Key={
                'ProductID': productName,
                'InstanceID': instance['InstanceID']
            }
        )

# TODO
#

# Survey db clusters  - for Aurora

# For local test execution
lambda_handler(0,0)
