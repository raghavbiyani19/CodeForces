t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    even=0
    odd=0
    for item in arr:
        if(item%2==0):
            even+=1
        else:
            odd+=1
    arr.sort()
    if(even%2==0 and odd%2==0):
        print("YES")
    else:
        flag=False
        for i in range(n-1):
            if(arr[i+1]-arr[i]==1):
                flag=True
                break
        if(flag==True):
            print("YES")
        else:
            print("NO")
    t-=1
