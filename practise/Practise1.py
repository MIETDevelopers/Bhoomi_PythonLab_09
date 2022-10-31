# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'bhoomi': '10', 'bunny': '9',
		'shuvam': '15', 'manyata': '2'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
