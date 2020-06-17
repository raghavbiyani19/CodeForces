t=int(input())
while(t!=0):
    n,k=map(int,input().split())
    if(n & 1):
        #ODD
        if(k & 1):
            if(k*k>n):
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
    
    else:
        #EVEN
        if(not k & 1):
            #EVEN
            if(k*k>n):
                print("NO")
            else:
                print("YES")
        else:
            #ODD
            print("NO")
    t-=1
