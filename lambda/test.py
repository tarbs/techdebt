import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

def lambda_handler(event, context):
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")

    # Open TechDebtReference table
    ref_table = dynamodb.Table('TechDebtReference')

    print("Get reference data")
    response = ref_table.scan()

    print("Found - ", response["Count"])

    print("Processing each item ...")

    ref_data = {}

    # ProductID         -> ProductID
    # VersionID         -> VersionID
    # ExpectedEoLDate   -> ExpectedEoLDays
    #                   -> ProductCount (calculated)

    date_format = "%Y%m%d"
    date_now = datetime.utcnow()

    for i in response['Items']:
        product_id = i['ProductID']
        version_id = i['VersionID']
        product_eol_date_str = i['ExpectedEoLDate']

        # ref_key = product_id + version_id

        try:
            data_item = ref_data[product_id]
            # pass
        except KeyError:
            data_item = {}
            #pass

        
        product_eol_date = datetime.strptime(product_eol_date_str, date_format)
        date_diff = product_eol_date - date_now

        ver_items = {}

        

        ver_item = {}
        ver_item['VersionID'] = version_id
        ver_item['ExpectedEoLDays'] = date_diff.days
        ver_item['ProductCount'] = 0
        print(ver_item)



        ref_item = {}
        ref_item['ProductID'] = product_id
        ref_item['VersionID'] = version_id
        ref_item['VersionInfo'] = ver_item
        print(ref_item)

        ref_data[ref_key] = ref_item

    print(ref_data)








    # Open TechDebtInstance table
    inst_table = dynamodb.Table('TechDebtInstance')

    print("Get instance data")
    response = inst_table.scan()

    print("Found - ", response["Count"])

    print("Processing each item ...")

    # ProductID
    # InstanceID
    # LastRecordedDatetime
    # VersionID
    for i in response['Items']:
        # print(i['ProductID'], ":", i['VersionID'])

        product_id = i['ProductID']
        version_id = i['VersionID']
        ref_key = product_id + version_id

        try:
            data_item = ref_data[ref_key]

            product_count = data_item['ProductCount']
            product_count = product_count + 1
            data_item['ProductCount'] = product_count
            # pass
        except KeyError:
            print("Product ", ref_key, "not found")
            #pass
        

    # print(ref_data)

    # json_data = json.dumps(ref_data)

    # print(json_data)

    target_data = []

    print(target_data)

    json_data = json.dumps(target_data)

    print(json_data)

lambda_handler (0,0)
