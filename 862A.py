n,x=map(int,input().split())
arr=list(map(int,input().split()))[:n]
ans=0
myMap={}
for i in range(n):
    myMap[arr[i]]=1
for i in range(x):
    if(myMap.get(i) is None):
        ans+=1
if(myMap.get(x) is not None):
    ans+=1
print(ans)
