from typing import List,Dict
import csv
import itertools


d = {"key1": [1,2,3,4], "key2": [4,5,6], "key3": [7,8,9]}
with open("tester.csv", "w") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(d.keys())
   writer.writerows(itertools.zip_longest(*d.values()))

