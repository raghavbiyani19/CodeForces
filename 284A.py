from math import gcd
n=int(input())
result=1
for i in range(2,n-1):
    if(gcd(i,n-1)==1):
        #print(i)
        result+=1
print(result)
