'''
#G- Little girl and game
import collections
inpS=str(input())
ansCount=0
myMap= collections.Counter(inpS)
for val in myMap.values():
	ansCount+=(val)%2

if ansCount==0 or ansCount%2==1:
    print("First")
else:
    print("Second")
'''
