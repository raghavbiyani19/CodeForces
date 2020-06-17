import math

def isPrime(n):
    flag=1
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            flag = 0
            break
    if (flag == 1):
        return True
    else:
        return False

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
ans=0
if(k==1 or l==1 or m==1 or n==1):
    print(d)
else:
    for i in range(1,d+1):
        if(i%k==0 or i%l==0 or i%m==0 or i%n==0):
           ans+=1
    print(ans)
