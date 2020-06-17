test=int(input())
while(test!=0):
    t=[]
    n=int(input())
    for i in range(n):
        a=list(input())
        t.append(a)
    flag=0
    #print(t)
    for i in range(n):
        for j in range(n):
            #print(i," ",j)
            if(t[i][j]=='1'):
                if((j!=n-1 and t[i][j+1]=='0') and (i!=n-1 and t[i+1][j]=='0')):
                    flag=1
                    break
    if(flag==0):
        print("YES")
    else:
        print("NO")
    test-=1
