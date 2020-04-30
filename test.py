import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

print(person)
print(person_dict)

print(person_dict['languages'][0])
print(person_dict["name"])

print(json.dumps(person_dict, indent = 4, sort_keys=True))
print(json.dumps(person, indent = 4, sort_keys=True))