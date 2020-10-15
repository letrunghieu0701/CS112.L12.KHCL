str_a = input().strip()
str_b = input().strip()
dic = set() # Tao dictonary luu tru cac cap ky tu
count = 0

for i in range(len(str_b) - 1): # Tach tung cap ky tu cua chuoi thu 2 vao dict
  key = str_b[i:i+2]
  dic.add(key) 
  
for i in range(len(str_a) - 1): # Tach tung cap ky tu cua chuoi thu 1 va xet xem co trong dict ko
   key = str_a[i:i+2]
   if (key in dic):
    count += 1
print(count)