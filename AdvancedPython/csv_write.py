f = open("data.csv", "w",newline="")

import csv

content = [
    ["name", "age", "place"],
    ["arun", 25, "ekm"],
    ["amal", 26, "tvm"],
]

# w=csv.writer(filereference)

w = csv.writer(f)

w.writerows(content)  # writes each row to the file
f.close()