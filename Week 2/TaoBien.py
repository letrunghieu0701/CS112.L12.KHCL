n, k = map(int, input().split())
fib = 2*k + 1
f = [0] * (fib+1) 

def findFibonacci(n):
    if (n == 0):
        return 1
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])
   
    if (f[n]): 
        return f[n]
  
    if(n & 1):
        k = (n + 1) // 2
    else :  
        k = n // 2

    if(n & 1):
        f[n] = (findFibonacci(k) * findFibonacci(k) + findFibonacci(k-1) * findFibonacci(k-1))
    else:
        f[n] = (2*findFibonacci(k-1) + findFibonacci(k))*findFibonacci(k)
  
    return f[n]

total = n*findFibonacci(fib)%(10**9+7)
print(total)