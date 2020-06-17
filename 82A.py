n=int(input())
myMap={0:"Sheldon",1:"Leonard",2:"Penny",3:"Rajesh",4:"Howard"}
n-=1
while(n>=5):
    n-=5
    n=n//2
print(myMap.get(n))
