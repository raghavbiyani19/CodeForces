n,k = input().split(" ")
n = int(n)
k = int(k)
if(n%2!=0):
    totalEven = int((n-1)/2)
    totalOdd = totalEven+1
else:
    totalEven = int(n/2)
    totalOdd = totalEven
if(k - totalOdd > 0):
    print(int(2*(k-totalOdd)))
else:
    print(int(2*k-1))