import heapq
n,k1,k2 = map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:n]
total=k1+k2
arr=[]
for i in range(n):
    arr.append((-1)*abs(a[i]-b[i]))
heapq.heapify(arr)
while(total>0):
    item=(-1)*(heapq.heappop(arr))
    heapq.heappush(arr,(-1)*abs(item-1))
    total-=1
ans=0
for i in range(len(arr)):
    ans+=(arr[i])**2
print(ans)
