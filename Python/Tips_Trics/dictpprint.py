import json
from pprint import pprint

sample_dict = {"name": "dinesh",
               "age":32,
               "stats":{"height":170,"weight":74},
               "mysets":{1,2,3,4,5}}

# Print using regular print
print(" The sample dict values are ", sample_dict)

# Print using the json module
print(json.dumps(sample_dict, indent=4, sort_keys=True, default= str))

# Print using the pprint module
pprint(sample_dict)