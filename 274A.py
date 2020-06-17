n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr.sort()
h={}
count=0
for i in range(n):
    h[arr[i]]=1
for i in range(n):
    if(h[arr[i]]!=0):
        if(arr[i]*k in h):
            h[arr[i]*k]=0
        count+=1
print(count)
