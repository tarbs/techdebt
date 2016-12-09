import boto3
import json

def lambda_handler(event, context):

    testdata = [
        {'a': 'aaa'},
        {'a': 'bbb'},
        {'a': 'ccc'},
        {'a': 'ddd'}
    ]

    s3 = boto3.resource('s3')

    outputObject = s3.Object('techdebt-website', 'processing/andytest')
    outputbuffer = ""

    for i in testdata:
        outputbuffer = outputbuffer + i['a']   

    outputbytes=bytearray(outputbuffer)
    print(outputbytes)
    outputObject.put(Body=outputbytes)


lambda_handler("","")