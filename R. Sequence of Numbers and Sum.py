import sys

for line in sys.stdin:
    x,y=map(int,line.split())

    if x<=0 or y<=0:
        break

    a=max(x,y)
    b=min(x,y)
    result=list(range(b,a+1))
    sum_num=sum(result)
    print(' '.join(map(str,result)), f"sum ={sum_num}")