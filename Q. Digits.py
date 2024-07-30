number=int(input())

for i in range(number):
    n=input()
    reverse_n=n[ :: -1]

    print(' '.join(reverse_n))