X=lambda:input().split(" ")[1:]
n=int(input())
nums=[]
for i in range (1,n+1):
    nums.append(str(i))
a = X()
b= X()
c = set(a+b)
d = set(nums)
if(len(d.difference(c)) == 0):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")