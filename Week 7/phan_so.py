import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a*d < c*b):
    number_of_steps = 0
    while (a*d < c*b):
        g = math.gcd(a+1, b+1)
        a = (a+1) // g
        b = (b+1) // g
        number_of_steps += 1
        if (a == c and b == d):
            print(number_of_steps)
            quit()
print(0)