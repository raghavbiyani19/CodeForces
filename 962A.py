n = int(input())
probs = list(map(int,input().split(" ")))[:n]
total = sum(probs)
sumProb=0
for i in range(n):
    sumProb+=probs[i]
    if(sumProb >= total/2):
        print(i+1)
        break