number=int(input())

for i in range(1,number+1):
    space=' '*(number-i)
    result='*'*(2*i-1)
    print(space+result)