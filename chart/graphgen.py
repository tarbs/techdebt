#!/usr/bin/python

import sys
import json
sys.path.insert(0,'/usr/lib/python2.7/site-packages/chartjs')
import chartjs

data = json.loads(open('data.json').read())
label = []
dataset = []

for i in data.keys():
    #labelname = '%s:%s' % (i, data[i]['ExpectedEoLDays']) 
    if 'Linux::JBoss' in i:
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
print(mychart.make_chart())
