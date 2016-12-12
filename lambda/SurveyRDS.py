
# Survey the current AWS account for running RDS instances and log the details into DynamoDB

import boto3
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
        # print(instance['DBInstanceIdentifier'] + ' ' +  instance['Engine'] + ' ' +  instance['EngineVersion'])
        productName = 'RDS::' + instance['Engine']
        instanceItem = {
            'ProductID': productName,
            'InstanceID': instance['DBInstanceIdentifier'],
            'VersionID': instance['EngineVersion'],
            'LastRecordedDatetime': dateStamp
        }
        # print(json.dumps(instanceItem))
    
        returnval = table.put_item(
            Item=instanceItem,
            ReturnValues='ALL_OLD'
        )
        print(returnval)
    

# TODO
#
# Survey db clusters  - for Aurora


