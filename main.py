import json
from User_Json import cleaned_response
with open('data1.json', 'w') as json_file:
    json.dump(cleaned_response, json_file, indent=4)