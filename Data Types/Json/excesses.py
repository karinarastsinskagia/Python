import json

#Convert json object to python object
json_obj =  '{ "Name":"George", "Age":"25", "Gender":"M" }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Student's Class: ",python_obj["Age"])
print("Age: ",python_obj["Gender"])
#
#Convert a python obs to a json obj
python_obj = {
  "name": "David",
  "Gender":"M",
  "age": 25
}
print(type(python_obj))
# convert into JSON:
json_obj = json.dumps(python_obj)

# # result is a JSON string:
print(json_obj)


# Read and write JSON files
with open('data.json', 'r') as file,  open('to.json', 'w') as destination:
    data = json.load(file)
    json.dump(data, destination)



