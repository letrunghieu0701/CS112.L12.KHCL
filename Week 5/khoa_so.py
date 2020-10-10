def findLargest(n, v): 
    flag = 0
    sum = 0
    
    for i in range(n): 
        if (v[i] == 0): 
            flag = 1
        sum += v[i] 
    v.sort(reverse = True)
    y = sum % 3
    if (y != 0):
        i = n - 1
        while(i >= 0):
            if (v[i] % 3 == y): 
                v.remove(v[i]) 
                flag = 1
                break
            i -= 1
        if (flag == 0):
            y = 3 - y
            cnt = 0
            i = n - 1
            while(i >= 0):
                if (v[i] % 3 == y): 
                    v.remove(v[i]) 
                    cnt += 1
                    if (cnt >= 2): 
                        break         
                i -= 1

    for i in (v): 
        print(i, end = "")
        
def split(arr): 
    return list(map(int, arr))

v = split(input())
n = len(v)
findLargest(n, v)