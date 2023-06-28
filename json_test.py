import json

employee = {"name": "Mike","age":55, "salary":4000,"isMarried": True, "HavingCar": None}

json_string= json.dumps(employee, indent=4)
print(json_string)

#with open("emp.json","w") as f:

#    json.dump(employee,f,indent=4)

emp_dict=json.loads(json_string)
print(type(emp_dict))

for key,value in emp_dict.items():
    print(key,":",value)