n = int(input())
counter=0
sum1=0
sum2=0
coins = list(map(int,input().split(" ")))[:n]
coins.sort(reverse = True)
for i in range(len(coins)):
    sum2=0
    sum1+=coins[i]
    for j in range(len(coins)-1,i,-1):
        sum2+=coins[j]
    counter+=1
    if(sum1>sum2):
        break
print(counter)