from __future__ import print_function
import boto3
import os
import sys
import uuid
import json
import inspect

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
sys.path.insert(0, cmd_folder + '/chartjs')

import chartjs

s3_client = boto3.client('s3')

def genchart(file_path, output_path):
    print(file_path, output_path)
    data = json.loads(open(file_path).read())
    label = []
    dataset = []
    for i in range(len(data['Versions'])):
       label.append(data['Versions'][i]['ExpectedEoLDays'])
       dataset.append(data['Versions'][i]['ProductCount'])

    mychart = chartjs.chart(data['ProductId'], "Bar", 640, 480)
    mychart.set_labels(label)
    mychart.add_dataset(dataset)
    mychart.set_params(fillColor = "rgba(220,220,220,0.5)", strokeColor = "rgba(220,220,220,0.8)", highlightFill = "rgba(220,220,220,0.75)", highlightStroke = "rgba(220,220,220,1)",)
    mychart.set_colors(['#FA0000', '#008811', '#0055FA', '#559090'])
    mychart.set_highlights(['#FF0000', '#00B851', '#0055FF', '#75B0B0'])
    #print(mychart.make_chart_full_html())
    of = open(output_path,"w")
    of.write(mychart.make_chart())


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        uploadbucket = 'techdebt-chartoutput'
        key = record['s3']['object']['key']
        print (key)
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '%s.%s' % (download_path, 'html')

        s3_client.download_file(bucket, key, download_path)
        genchart(download_path, upload_path)
        s3_client.upload_file(upload_path, uploadbucket, key)
