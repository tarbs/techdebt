import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

localdbg = 0

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")

    # Open TechDebtReference table
    ref_table = dynamodb.Table('TechDebtReference')

    print("Get reference data")
    response = ref_table.scan()

    print("Found - ", response["Count"])

    print("Processing each item ...")

    ref_data = {}

    date_format = "%Y%m%d"
    date_now = datetime.utcnow()

    for i in response['Items']:
        product_id = i['ProductID']
        version_id = i['VersionID']
        product_eol_date_str = i['ExpectedEoLDate']

        product_eol_date = datetime.strptime(product_eol_date_str, date_format)
        date_diff = product_eol_date - date_now

        try:
            data_item = ref_data[product_id]
            # pass
        except KeyError:
            data_item = {}
            data_item['ProductID'] = product_id
            #pass

        try:
            ver_items = data_item['Versions']
            # pass
        except KeyError:
            ver_items = {}
            data_item['Versions'] = ver_items
            #pass
        
        ver_item = {}
        ver_item['VersionID'] = version_id
        ver_item['ExpectedEoLDays'] = date_diff.days
        ver_item['ProductCount'] = 0
        print(ver_item)

        ver_items[version_id] = ver_item

        print(data_item)

        ref_data[product_id] = data_item

    print(ref_data)








    # Open TechDebtInstance table
    inst_table = dynamodb.Table('TechDebtInstance')

    print("Get instance data")
    response = inst_table.scan()

    print("Found - ", response["Count"])

    print("Processing each item ...")

    for i in response['Items']:

        product_id = i['ProductID']
        version_id = i['VersionID']

        try:
            data_item = ref_data[product_id]
            product_versions = data_item['Versions']

            try:
                ver_item = product_versions[version_id]
                product_count = ver_item['ProductCount']
                product_count = product_count + 1
                ver_item['ProductCount'] = product_count

            except KeyError:
                print("Version ", version_id, " for product ", product_id, " not found")
            
            # pass
        except KeyError:
            print("Product ", product_id, " not found")
            #pass
        

    # print(ref_data)

    # json_data = json.dumps(ref_data)

    # print(json_data)

    target_data = []

    for key, value in ref_data.iteritems():
        product_id = key
        ver_items = value['Versions']

        item_data = {}
        ver_array = []

        item_data['ProductId'] = product_id
        item_data['Versions'] = ver_array

        for vkey, vvalue in ver_items.iteritems():
            version_id = vvalue['VersionID']
            expected_eol_days = vvalue['ExpectedEoLDays']
            product_count = vvalue['ProductCount']

            ver_item = {}
            ver_item['VersionId'] = version_id
            ver_item['ExpectedEoLDays']= expected_eol_days
            ver_item['ProductCount']= product_count

            ver_array.append(ver_item)

        target_data.append(item_data)

        json_data = json.dumps(item_data)
        t = datetime.utcnow()
        
        file_name = product_id # + t.strftime('%Y%m%d%H%M%S')

        if localdbg == 0:
            print(json_data)
            outputObject = s3.Object('techdebt-jsonoutput', file_name)
            outputbytes=bytearray(json_data)
            # print(outputbytes)
            outputObject.put(Body=outputbytes)


    print(target_data)

    json_data = json.dumps(target_data)

    print(json_data)

if localdbg == 1:
    lambda_handler (0,0)
