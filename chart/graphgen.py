#!/usr/bin/python

from __future__ import print_function
import boto3
import os
import sys
import uuid
import chartjs
import json

s3_client = boto3.client('s3')

def genchart(file_path, output_path):
    data = json.loads(open(file_path).read())
    label = []
    dataset = []
    for i in data.keys():
        productname = i
        label.append(data[i]['ExpectedEoLDays'])
        dataset.append(data[i]['ProductCount'])

    mychart = chartjs.chart(productname, "Bar", 640, 480)
    mychart.set_labels(label)
    mychart.add_dataset(dataset)
    mychart.set_params(fillColor = "rgba(220,220,220,0.5)", strokeColor = "rgba(220,220,220,0.8)", highlightFill = "rgba(220,220,220,0.75)", highlightStroke = "rgba(220,220,220,1)",)
    mychart.set_colors(['#FA0000', '#008811', '#0055FA', '#559090'])
    mychart.set_highlights(['#FF0000', '#00B851', '#0055FF', '#75B0B0'])
    #print(mychart.make_chart_full_html())
    outfile = open('output_path','w')
    outfile.write(mychart.make_chart())

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/graph-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        genchart(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}graph'.format(bucket), key)
