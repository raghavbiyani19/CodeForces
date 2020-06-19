n=int(input())
graph={}
countD={}
for i in range(n-1):
    x,y=map(int,input().split())
    if x in graph:
        graph[x].add(y)
        countD[x]+=1
    else:
        graph[x]={y}
        countD[x]=1

    if y in graph:
        graph[y].add(x)
        countD[y]+=1
    else:
        graph[y]={x}
        countD[y]=1
#print(graph)
seq=list(map(int,input().split()))
if seq[0]!=1:
    print("No")
else:
    i=0
    j=0
    flag=0
    while j!=n-1:
        l=countD[seq[i]]
        if seq[i]!=1:
            l-=1
        f=0
        for x in range(j+1,j+1+l):
            if seq[x] not in graph[seq[i]]:
                f=1
                break
        if f==1:
            flag=1
            break
        else:
            i+=1
            j+=l
    if flag==1:
        print("No")
    else:
        print("Yes")
