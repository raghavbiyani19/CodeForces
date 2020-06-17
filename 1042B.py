def getSum(x,y):
    if(myMap.get(x) is None or myMap.get(y) is None):
        return float("inf")
    else:
        return myMap.get(x)+myMap.get(y)
    
n=int(input())
myMap={}
for i in range(n):
    temp=list(map(str,input().split()))
    strList=[]
    for x in temp[1]:
        strList.append(x)
    strList.sort()
    temp[1]="".join(strList)
    if(temp[1] not in myMap.keys()):
        myMap[temp[1]]=int(temp[0])
    else:
        myMap[temp[1]]=min(int(temp[0]),myMap[temp[1]])
ans=float("inf")
if(myMap.get("A") is not None and myMap.get("B") is not None and myMap.get("C") is not None):
    ans = myMap.get("A")+myMap.get("B")+myMap.get("C")
if(myMap.get("ABC") is not None):
    ans=min(ans,myMap.get("ABC"))
ans=min(ans,getSum("AB","C"))
ans=min(ans,getSum("A","BC"))
ans=min(ans,getSum("AC","B"))
ans=min(ans,getSum("AB","BC"))
ans=min(ans,getSum("AC","BC"))
ans=min(ans,getSum("AC","AB"))
if(ans==float("inf")):
    print(-1)
else:
    print(ans)
