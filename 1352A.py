t=int(input())
while(t!=0):
    n=int(input())
    nStr = str(n)
    count=0
    ans=[]
    for i in range(len(nStr)-1,-1,-1):
        tmp=nStr[i]
        if(tmp!="0"):
            count+=1
            toAdd = int(tmp)*(10**(len(nStr)-i-1))
            ans.append(toAdd)
    print(count)
    print(*ans,sep=" ")
    t-=1
