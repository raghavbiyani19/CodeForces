n=int(input())
arr=list(map(int,input().split()))
binary=[0]*20
for val in arr:
      temp=0
      while(val):
            if(val & 1):
                  binary[temp]+=1
            val>>=1
            temp+=1
ans=0
for i in range(n):
      temp=0
      for place in range(20):
            if(binary[place]):
                  temp+=(1<<place)
                  binary[place]-=1
      ans+=(temp**2)
print(ans)
