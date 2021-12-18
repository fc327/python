import os
import json
import requests

file = 'summer21olympics.json'
with open(file) as f:
    olympicdata = json.load(f)
print(len(olympicdata))

type(olympicdata)
olympicdata.keys()

sportinfo = olympicdata['Discipline']
len(sportinfo)

sportinfo['00e2cff7-ab78-311d-8e14-079dec40050a']['attributes']['description']
