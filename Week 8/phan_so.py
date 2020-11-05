import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a*d < b*c):
    number_of_steps = 0
    while (a*d <= b*c):
        g = math.gcd(a + 1, b + 1)  # tìm ước chung của a++ và b++ để tìm xem có thể tối giản phân số đc ko
        a = (a + 1)//g              # nếu g > 1 => có thể tối giản được
        b = (b + 1)//g
        number_of_steps += 1
        if (a == c and b == d):
            print(number_of_steps)
            quit()
print(0)