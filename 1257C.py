#D-Dominated subarray
t=int(input())
while(t!=0):
    n=int(input())
    arr=[int(x) for x in input().split()]
    myMap=defaultdict(int)
    ans=n+1
    for i in range(n):
        if(myMap.get(arr[i]) is None):
            myMap[arr[i]]=i
        else:
            ans=min(ans,i-myMap.get(arr[i])+1)
            myMap[arr[i]]=i
    if(ans>n):
    print(-1)
    else:
    print(ans)
    t-=1
