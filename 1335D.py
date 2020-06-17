t=int(input())
while(t!=0):
    myList=[]
    for i in range(9):
        myList.append(list(map(int,input().split())))
    for i in range(9):
        myStr=str(*myList[i])
        for j in range(9):
            if(myStr[j]=='7'):
                myStr=myStr[:j]+"1"+myStr[j+1:]
                myList[i]=myStr
                break
    for i in range(9):
        print(*myList[i],sep="")
    t-=1
