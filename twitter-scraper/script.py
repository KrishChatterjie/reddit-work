import json

with open('test.json') as f:
    mydata = json.load(f)

with open('test.json', 'w') as outfile:
    json.dump(mydata, outfile, indent=4)