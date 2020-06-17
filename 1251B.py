t=int(input())
while(t!=0):
  n=int(input())
  odd=0
  evenGood=0
  evenBad=0
  for i in range(n):
    s=str(input())
    if(len(s) & 1):
      odd+=1
    else:
      if(s.count("1") & 1):
        evenBad+=1
      else:
        evenGood+=1
  if(odd==0 and (evenBad & 1)):
    print(n-1)
  else:
    print(n)
  t-=1
