x,y = map(int,input().split(" "))
if(y == 0):
    print("NO")
elif(y==1):
    if x==0:
        print("YES")
    else:
        print("NO")
else:
    z = x-y+1
    if(z<0):
        print("NO")
    else:
        if(z%2==0):
            print("YES")
        else:
            print("NO")