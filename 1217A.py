mylist=[]
t = int(input())
for i in range(t):
    mylist.append(list(map(int,input().split(" ")))[:3])
for i in range(t):
    ans=0
    if(mylist[i][0] + mylist[i][2] > mylist[i][1]):
        if(mylist[i][1] >= mylist[i][0]):
            mylist[i][2] -= mylist[i][1] - mylist[i][0] + 1
            mylist[i][0] = mylist[i][1] + 1
        diff = mylist[i][0] + mylist[i][2] - mylist[i][1]
        ans = min(mylist[i][2] + 1, int(diff / 2) + int(diff % 2))
    print(ans)