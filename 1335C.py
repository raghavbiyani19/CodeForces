t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    uniqueCount=0
    myMap={}
    for i in range(n):
        if(myMap.get(arr[i]) is None):
            uniqueCount+=1
            myMap[arr[i]]=1
        else:
            myMap[arr[i]]+=1
    sameCount=max(myMap.values())
    if(sameCount==uniqueCount-1):
        print(sameCount)
    else:
        print(max(min(sameCount,uniqueCount-1),min(sameCount-1,uniqueCount)))
    t-=1
