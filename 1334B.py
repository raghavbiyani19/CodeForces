#A-Middle class
t=int(input())
while(t!=0):
  n,x=map(int,input().split())
  arr=list(map(int,input().split()))[:n]
  arr.sort(reverse=True)
  if(arr[0]<x):
    print(0)
  else:
    i=1
    average=arr[0]
    temp=arr[0]
    while(average>=x and i<n):
      av=(arr[i]+temp)//(i+1)
      if(av>=x):
        temp+=arr[i]
        average=av
      else:
        break
      i+=1
    print(i)
  t-=1
