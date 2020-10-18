from typing import List,Dict
import csv
import itertools

import re

string = 'This is laughing laugh'

a = re.search(r'\b(is)\b', string)
print(a.start())
