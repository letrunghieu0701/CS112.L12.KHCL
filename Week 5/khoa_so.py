s = input().strip()

count = [0]*10
for i in s:
    count[int(i)]+=1
    
sum = 0
for i in range(10):
    sum += i*count[i]
    
mod_2 = []
mod_1 = []
for i in range(1,9):
    if i % 3 == 1:
        mod_1+=[i]*count[i]
    if i % 3 == 2:
        mod_2+=[i]*count[i]
        
if(sum % 3 == 2):
    if len(mod_2) > 0:
        count[mod_2[0]] -= 1
    else:
        count[mod_1[0]] -= 1
        count[mod_1[1]] -= 1

elif(sum % 3 == 1):
    if len(mod_1) > 0:
        count[mod_1[0]] -= 1
    else: 
        count[mod_2[0]] -= 1
        count[mod_2[1]] -= 1
        
s = ''
a = list(range(10))
a.reverse()

for x in a:
    s+=str(x)*count[x]
    
print(s)
