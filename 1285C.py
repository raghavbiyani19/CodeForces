from math import gcd
def lcm(n1,n2):
    return n1/gcd(n1,n2) *n2
def getfactors(a,factor):
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            if(max(factor)>max(i,int(a/i)) and lcm(i,int(a/i))==a):
                factor[0]=i
                factor[1]=int(a/i)
a=int(input())
factor=[1,a]
getfactors(a,factor)
print(*factor,end=" ")
