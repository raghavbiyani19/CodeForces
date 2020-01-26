feeling1="I hate that "
feeling2="I love that "
n = int(input())
answer =""
for i in range(1,n+1):
    if(i!=n):
        if(i!=1):
            if(i%2==0):
                answer = answer + feeling2
            else:
                answer = answer + feeling1
        else:
            answer = answer + "I hate that "
    else:
        if(i!=1):
            if(i%2==0):
                answer = answer + "I love it"
            else:
                answer = answer + "I hate it"
        else:
            answer = answer + "I hate it"
print(answer)