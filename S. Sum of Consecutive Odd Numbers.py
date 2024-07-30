number=int(input())

for i in range(number):
    x,y=map(int,input().split())

    a=min(x,y)
    b=max(x,y)
    sum_n=0
    for w in range(a+1,b):
        if w%2 !=0:
            sum_n+=w
    print(sum_n)
