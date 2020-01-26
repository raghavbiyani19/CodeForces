n,k = input().split(" ")
n= int(n)
k= int(k)
while(k!=0):
    lastDigit = n%10
    if lastDigit==0:
        n=n/10
    else:
        n=n-1
    k=k-1
print(int(n))