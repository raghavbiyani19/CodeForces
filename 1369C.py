t=int(input())
while(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    w=list(map(int,input().split()))
    arr.sort(reverse=True)
    w.sort(reverse=True)
    singles=w.count(1)
    total=0
    for i in range(singles):
        total+=(2*(arr[i]))
    j=n-1
    for i in range(k-singles):
        total+=arr[singles]+arr[j]
        singles+=1
        j=j-w[i]+1
    print(total)
    t-=1
