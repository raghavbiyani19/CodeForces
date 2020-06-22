n,r= map(int, input().split())
arr=list(map(int, input().split()))
cur=0
res=0
while(cur<n):
    b=max(0,cur-r+1)
    c=arr[b:cur+r]
    if sum(c)!=0:
        i=len(c)-c[-1::-1].index(1)-1
        cur=b+i+r
        res+=1
    else:
        print(-1)
        break
else:
    print(res)
