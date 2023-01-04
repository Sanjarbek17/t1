import requests
import json
import sys

url = 'https://codeschoolhomeworkapi.pythonanywhere.com/'

f = open('data.json', 'r')
data = json.load(f)
dct = {
    "github": sys.argv[1],
    "repo": sys.argv[2],
    "tasks": data
}

f.close()
r = requests.post(url+'homework/attempt/', json=dct)
# print(r)
corrects = 0
for answer in data:
    corrects += answer['isSolved']

print('=' * 8 + ' Natijalar: ' + '=' * 8)
    # Print readability report
for task in data:
    # task_name=results[t]
    
    if task['isSolved']:
        print(
            f'{task["name"]}  Passed:{task["details"]["passed"]} Failed:{task["details"]["failed"]} ✅')
    else:
        print(f'{task["name"]}  Passed:{task["details"]["passed"]} Failed:{task["details"]["failed"]} ❌')

 
# Check if all tasks are solved otherwise raise error
if corrects == len(data):
    print('All tasks are solved')
    print('Barcha vazifalar topshirildi')
else:
    print('Not all tasks are solved')
    print('Barcha vazifalar topshirilmagan')
    sys.exit(1)