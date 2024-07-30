number=int(input())

x=0
y=1

if number>0:
    print(x,end=' ')

if number>1:
    print(y,end=' ')

for i in range(2,number):
    sum_num=x+y
    print(sum_num,end=' ')
    x=y
    y=sum_num
