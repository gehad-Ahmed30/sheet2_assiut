number=int(input())

for i in range(number):
    n=int(input())
    x=bin(n).count('1')
    y='1'*x
    result=int(y,2)
    print(result)