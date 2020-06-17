def check(a,final):
    count=0
    for i in range(len(a)):
        for j in range(len(final)):
            if(final[j]!=a[i][j]):
                count+=1
        if(count>1):
            return False
        else:
            count=0
    return True
 
test=int(input())
while(test!=0):
    n,m=[int(x) for x in input().split()]
    a=[]
    for i in range(n):
        a.append(input())
    final=a[0]
    flag=0
    for i in range(m):
        for j in range(97,123):
            x=chr(j)
            #print(x,"  ",final)
            final=final[:i]+x+final[i+1:]
            if(check(a,final)==True):
                print(final)
                flag=1
                break     
        final=final[:i]+a[0][i]+final[i+1:]
        if(flag==1):
            break
    #print("here")
    if(flag==0):
        print(-1)
    test-=1
