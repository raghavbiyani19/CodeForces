n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
count=0
temp=1
i=0
while(i<n-1):
    if l[i]==l[i+1]:
        temp*=l[i]
        i+=2
        count+=1
    elif l[i]==(l[i+1]+1):
        temp*=l[i+1]
        i+=2
        count+=1
    else:
        i+=1
    if count==2:
        count=0
        ans+=temp
        temp=1
print(ans)
