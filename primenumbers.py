def is_prime(x):
    dels = []
    for i in range(2, x//2+1):
        if x%i == 0:
            dels.append(i)
    print(dels)
    if len(dels) > 0:
        return False
    else:
        return True

while True:
    p = int(input())
    if p < 2:
        exit()
    else:
        print(is_prime(p))