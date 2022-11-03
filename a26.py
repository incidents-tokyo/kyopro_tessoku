def is_prime(x):
    i=2
    while True:
        if i*i>x:
            break
        if x%i==0:
            return False
        i+=1
    return True
Q = int(input())
for _ in range(Q):
    X = int(input())
    print("Yes" if is_prime(X) else "No")