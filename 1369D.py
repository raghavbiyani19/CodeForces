MAX=(10**9)+7
dp=[0]*(2000000+1)
dp[3]=1
dp[4]=1
for i in range(5,2000001):
    if(i%3 == 0):
        dp[i]=(dp[i-1]+(2*dp[i-2])+1)%MAX
    else:
        dp[i]=(dp[i-1]+(2*dp[i-2]))%MAX
t=int(input())
while(t):
    n=int(input())
    MAX=(10**9)+7
    ans=dp[n]
    print((ans*4)%MAX)
    t-=1
