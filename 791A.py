a,b = input().split(" ")
a = int(a)
b = int(b)
i=1
while(True):
    a = 3*a
    b = 2*b
    if(a>b):
        break
    else:
        i=i+1
print(i)