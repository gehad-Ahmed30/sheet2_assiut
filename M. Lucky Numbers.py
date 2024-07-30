number = input()

x, y = map(int, number.split())

found_lucky = False  

for i in range(x, y + 1):
    flag_lucky = True
    n = i
    while n > 0:
        digit = n % 10
        if digit != 4 and digit != 7:
            flag_lucky = False
            break  
        n //= 10
    
    if flag_lucky:
        print(i, end=' ')
        found_lucky = True

if not found_lucky:
    print(-1)

