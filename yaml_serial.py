from pyaml import yaml

emp_dict = {'name': 'John', 'age': 40, 'salary':5000, 'isMarried':True}

yaml_string=yaml.dump(emp_dict)
print(yaml_string)

with open('emp.yaml','w') as f:
    yaml.dump(emp_dict,f)

e_dict = yaml.safe_load(yaml_string)
print(e_dict)

with open('emp.yaml','r') as f:
    e_dict_f=yaml.safe_load(f)

print(e_dict_f)