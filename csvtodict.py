# with open("cities.csv", "r") as f:
#     res = []
#     for lines in f:
#         line = lines.split(",")
#         res.append((line[0], line[1:]))
#     print(res)


# import csv
# reader = csv.reader(open('cities.csv', 'r'))
# print(reader)
    
# import pandas as pd

# df = pd.read_csv('cities.csv')
# print(df)
import csv
with open('cities.csv') as f:
    d = dict(filter(None, csv.reader(f)))

print(d)
