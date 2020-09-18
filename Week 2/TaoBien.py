n, k = map(int, input().split())
fib = 2*k + 1
f = [0]*(fib + 1) 

def findFibonacci(n):
    if n == 0:
        return 1
    if n == 1 or n == 2:
        f[n] = 1
        return (f[n])
    
    if n & 1:
        temp = (n + 1) // 2
        f[n] = findFibonacci(temp)*findFibonacci(temp) + findFibonacci(temp-1)*findFibonacci(temp-1)
    else :  
        temp = n // 2
        f[n] = (2*findFibonacci(temp-1) + findFibonacci(temp)) * findFibonacci(temp)

    return f[n]

total = n * findFibonacci(fib) % (10**9+7)
print(total)