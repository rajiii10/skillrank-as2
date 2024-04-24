import json

file = open('ex5.json', 'r')
sample1 = json.load(file)
file.close()  

for i in sample1:
    if i["name"] == "Old Fashioned" and i["type"] == "donut": 
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(sample1, file, indent=2)
file.close()  