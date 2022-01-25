import json
from math import sin, cos, sqrt, atan2, radians

radius = 6371
distance = 0

f = open('dataset.json')
data = json.load(f)

final_dataset = []
count = 0

population_limit = 57100
for i in data:
    if i['population'] >= population_limit and count < 20 and i['name'] !="India" and i['name'] !="USA" and i['currencies'][0] != '' :
        if not i['latlng']:
            t = (0,0)
        else:
            t = (radians(i['latlng'][0]),radians(i['latlng'][1]))
        final_dataset.append(t)
        count = count + 1

for i,j in zip(range(0,20),range(1,20)):
    latitude = final_dataset[i][0]
    longtitude = final_dataset[i][1]
    latitude2 = final_dataset[j][0]
    longtitude2 = final_dataset[j][1]
    difflat = latitude2 - latitude
    difflong = longtitude2 - longtitude

    a = sin(difflat / 2)**2 + cos(latitude) * cos(latitude2) * sin(difflong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    temp = radius * c
    temp = round(temp,2)
    print(temp)
    distance = round(distance + temp,2)
    

print("Total Distance:", distance ,'km')
f.close()
