t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    i=1
    j=n-1
    turn=1
    player0=arr[0]
    player1=0
    chances=1
    eatenInMove0=arr[0]
    eatenInMove1=0
    discnt=0
    #print("YO")
    if(n==1):
        print(1,player0,player1)
    else:
        while(discnt==0):
            #print("CHANCE NUMBER:",chances+1)
            if(turn == 0):
                #print("PLAYER 0 CHANCE")
                while(eatenInMove0<=eatenInMove1 and i<=j):
                    #print("PLAYER 0 EATS",arr[i])
                    if(i==j):
                        discnt=1
                    player0+=arr[i]
                    eatenInMove0+=arr[i]
                    i+=1
                #print("PLAYER 0 TOTAL=",player0)
                eatenInMove1=0
                turn=1
                chances+=1
            else:
                #print("PLAYER 1 CHANCE")
                while(eatenInMove1<=eatenInMove0 and i<=j):
                    #print("PLAYER 1 EATS",arr[j])
                    if(i==j):
                        discnt=1
                    player1+=arr[j]
                    eatenInMove1+=arr[j]
                    j-=1
                #print("PLAYER 1 TOTAL=",player1)
                eatenInMove0=0
                turn=0
                chances+=1
        print(chances,player0,player1)
    t-=1
