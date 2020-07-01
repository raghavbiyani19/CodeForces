from collections import defaultdict
t=int(input())
while(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    myMap=defaultdict(int)
    for val in arr:
        modVal=val%k
        if modVal==0:
            continue
        myMap[modVal]+=1
    cnt=0
    for val in myMap:
        cnt=max(cnt,myMap[val]*k-val)
    print(cnt+1 if cnt!=0 else 0)
    t-=1
