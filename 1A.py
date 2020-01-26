n,m,a = input().split(" ")
n = int(n)
m = int(m)
a = int(a)
if(n*m <= a*a):
    print(1)
else:
    if(n%a == 0 and m%a==0):
        print(int((n*m)/(a*a)))    
    elif(n%a == 0 and m%a != 0):
        print(int(n/a * (int(m/a)+1)))
    elif(n%a != 0 and m%a == 0):
        print(int((int(n/a)+1) * m/a))
    else:
        print((int(n/a)+1) * (int(m/a)+1))