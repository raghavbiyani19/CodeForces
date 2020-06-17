def revOP(op):
    if(op=="<"):
        return ">="
    if(op=="<="):
        return ">"
    if(op==">"):
        return "<="
    if(op==">="):
        return "<"
    
n=int(input())
left=(-2)*(10**9)
right=(2)*(10**9)
for i in range(n):
    arr=list(map(str,input().split()))
    num=int(arr[1])
    oper=arr[0]
    
    if(arr[2]=="N"):
        oper=revOP(oper)
        
    if(oper==">="):
        if(left<num):
            left=num
    elif(oper==">"):
        if(left<num+1):
            left=num+1
    elif(oper=="<="):
        if(right>num):
            right=num
    elif(oper=="<"):
        if(right>num-1):
            right=num-1
 
if(left<=right):
    print(left)
else:
    print("Impossible")
