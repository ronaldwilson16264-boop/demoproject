import csv
f = open("data.csv", "r")
r = csv.reader(f)
for i in r:
  print(i)

f.close()