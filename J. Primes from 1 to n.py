number=int(input())

for i in range(2,number+1):   #for loop number
    flag_prime=True
    for x in range(2,int(i/2)+1):  #for loop prime
        if i%x==0:         #number/prime
            flag_prime=False
            break
        else:
            flag_prime=True
    if flag_prime:
        print(i,end=' ')

