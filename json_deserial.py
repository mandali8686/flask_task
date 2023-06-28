import json

with open('emp.json','r') as f:
    emp_dict=json.load(f)

print(type(emp_dict))

for key, value in emp_dict.items():
    print(key,":",value)