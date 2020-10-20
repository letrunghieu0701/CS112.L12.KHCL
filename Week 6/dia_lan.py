n, k = map(int, input().split())
a = tuple(map(bin, map(int, input().split()))) # Convert toan bo so thap phan sang nhi phan

# a toi da bang 2^12 => a tu 0 toi 4095 ma 4095 co do dai 12 bit
MAX_BIT_LENGTH = 13

def addNumber(a, bin_num):
    bin_num = bin_num[2:]
    bin_len = len(bin_num)
    for i in range(bin_len):
        a[i + MAX_BIT_LENGTH - bin_len] += int(bin_num[i])
    
def subNumber(a, bin_num):
    bin_num = bin_num[2:]
    bin_len = len(bin_num)
    for i in range(bin_len):
        a[i + MAX_BIT_LENGTH - bin_len] -= int(bin_num[i])

def get_result():
    count = [0 for __ in range(MAX_BIT_LENGTH)] # Tao mang co 12 phan tu vs gia tri ban dau moi phan tu bang 0
    for i in range(k):
        addNumber(count, a[i])
    
    found = False
    for i in range(1, n - k + 1):
        if k not in count:
            found = True
            break
        subNumber(count, a[i - 1])
        addNumber(count, a[i + k - 1])
    if k not in count:
        found = True
    
    if found:
        print("YES")
    else:
        print("NO")

get_result()