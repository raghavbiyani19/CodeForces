n=int(input())
arr=list(map(int,input().split()))[:n]
flag=0
for i in range(n):
    if(arr[i] & 1):
        flag=1
        break
if(flag==1):
    print("First")
else:
    print("Second")
