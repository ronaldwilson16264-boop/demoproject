f = open("data.json", "w")
import json
content = [
    {"name": "arun", "age": 23},
    {"name": "amal", "age": 24},
]


json.dump(content, f)

f.close()