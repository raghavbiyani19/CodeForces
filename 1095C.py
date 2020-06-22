#E- Powers of two
n,k=map(int,input().split())
arr=[1]*k
summ=k
for i in range(k):
  while(summ+arr[i]<=n):
      summ=summ+arr[i]
      arr[i]<<=1
if sum(arr)==n:
    print("YES")
    print(*arr,sep=" ")
else:
    print("NO")
