name= { 'a1':5, 'a2':4,'a3':7,'a4':2,'a5':5,'a6':4,'a7':5,'a8':2,'a9':7}
g=[]
k=[]
import collections


values= [_ for _, count in collections.Counter(name.values()).items()  if count==2 ]
tuple(values)

for key,value in name.items():

	if value in values :
		g.append(key)

#print(values)
print(g)
m= (tuple(g))
print(m)

print(set(m))

'''from solution import *
from utils import *

for unit in unitlist:
	for box in [unit]:
		if len(values[box])==2:
			k.append(box)
			print(k)
'''