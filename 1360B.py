t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    arr.sort()
    minD=float("inf")
    for i in range(n-1):
        minD=min(abs(arr[i]-arr[i+1]),minD)
    print(minD)
    t-=1
