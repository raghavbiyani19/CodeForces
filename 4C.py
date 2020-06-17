n=int(input())
a=[]
for i in range(n):
    a.append(input())
h={}
for i in range(n):
    if(a[i] in h.keys()):
        print(a[i]+str(h[a[i]]))
        h[a[i]]+=1
    else:
        print("OK")
        h[a[i]]=1
