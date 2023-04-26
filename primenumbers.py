def is_prime(x):
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True

while True:
    p = int(input())
    print(is_prime(p))