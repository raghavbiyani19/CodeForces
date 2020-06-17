t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    s=set(arr)
    ans=0
    temp=0
    for i in range(1,1025):
        flag=0
        newSet=set()
        for item in s:
            newSet.add(item)
        for j in range(n):
            val=i^arr[j]
            if(val not in newSet):
                flag=1
                break
            else:
                newSet.remove(val)
        if(flag==0):
            temp=1
            ans=i
            break
    if(temp==1):
        print(ans)
    else:
        print(-1)
    t-=1
