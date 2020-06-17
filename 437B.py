def check(num):
    x=str(bin(num))
    j=-1
    for i in range(len(x)-1,-1,-1):
        j+=1
        if(x[i]=='1'):
            break
    return j
s,limit=[int(x) for x in input().split()]
res=[]
for i in range(1,limit+1):
    x=check(i)
    res.append([2**x,i])
res.sort(key=lambda x:x[0])
#print(res)
ans=[]
for i in range(len(res)-1,-1,-1):
    if(s>=res[i][0]):
        s-=res[i][0]
        ans.append(res[i][1])
    if(s==0):
        break
if(s!=0):
    print(-1)
else:
    print(len(ans))
    print(*ans,sep=" ")
