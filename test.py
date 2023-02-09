import requests


BASE = 'http://127.0.0.1:5000/'

getres = requests.get(BASE+'video/0')
getresjson = getres.json()
print(f"first GET response: {getres.json()}")

input()

data = [
    {'likes': 10, 'name': 'Tim', 'views': 10000},
    {'likes': 20, 'name': 'Bill', 'views': 20000},
    {'likes': 30, 'name': 'Jill', 'views': 30000},
]


print(f"SET response:")

for i in range(len(data)):
    response = requests.put(BASE+'video/'+str(i), data[i])
    print(response.json())


print('GET after inserting DATA:')
for i in range(len(data)):
    print (requests.get(BASE+'video/'+str(i)).json())


if input() == 'update':
    patchResponse = requests.patch(BASE+'video/1', {'views': 1000000})
    print(patchResponse.json())

print('GET after patching:')

for i in range(len(data)):
    print (requests.get(BASE+'video/'+str(i)).json())
#response1 = requests.get(BASE+'video/0')
#print(response1.json())