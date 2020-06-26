n,b,a=map(int,input().split())
tempA=a+1
ans=0
sun=list(map(int,input().split()))[:n]
for i in range(n):
    if(sun[i]==1):
        #print("SUNLIGHT")
        if(a==tempA-1):
            #print("USING ACCUMULATOR")
            a-=1
            ans+=1
        elif(b>0):
            #print("USING BATTERY")
            b-=1
            a=(a+1)%tempA
            ans+=1
        elif(a>0):
            #print("USING ACCUMULATOR")
            a-=1
            ans+=1
        else:
            break
    else:
        #print("DARK")
        if(a>0):
            ans+=1
            #print("USING ACCUMULATOR")
            a-=1
        elif(b>0):
            ans+=1
            #print("USING BATTERY")
            b-=1
        else:
            #print("QUITTING")
            break
print(ans)
