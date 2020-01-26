n,m,a,b = input().split(" ")
n = int(n)
m = int(m)
a = int(a)
b = int(b)
numSpecial = int((n - n%m)/m)
if( n>m and (a <= b/m) ):
    print( n*a )
elif(n>m and (a > b/m) and a>=b):
    if( (n- (numSpecial*m)) != 0):
        print( (numSpecial*b) + (b) )
    else:
        print( (numSpecial*b) )
elif(n>m and (a > b/m) and a<b):
    print( (numSpecial*b) + (n- (numSpecial*m))*a )
elif(m>n and n*a < b):
    print(n*a)
else:
    print( b )