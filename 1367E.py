import math
from collections import defaultdict
def getDivisors(n):
    i=1
    ans=[]
    while(i<=math.sqrt(n)):
        if(n%i==0):
            if(n/i==i): 
                ans.append(i) 
            else:
                ans.append(i)
                ans.append(n//i)
        i=i+1
    return ans

t=int(input())
while(t!=0):
    n,k=map(int, input().split())
    s=str(input())
    maxx=0
    freq=defaultdict(int)
    for i in range(n):
        freq[s[i]]+=1
    fact=getDivisors(k)
    for lenn in fact:
        for l in range(lenn,n+1,lenn):
            possible=0
            each=l//lenn
            for f in freq.values():
                possible+=f//each
            if(possible>=lenn):
                maxx=max(maxx,l)
            else:
                break
    print(maxx)
    t-=1
