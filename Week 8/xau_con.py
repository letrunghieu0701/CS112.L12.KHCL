from sys import stdin, stdout

s = stdin.readline().strip()
q = int(input())

H = [0]

for char in s:
    H.append(H[-1] + hash(char))
    
def get_hash(a, b):
    return H[b] - H[a-1]

for _ in range(q):
    a, b, c, d = map(int, stdin.readline().split())
    if get_hash(a,b) == get_hash(c,d):
        print("YES")
    else:
        print("NO")

