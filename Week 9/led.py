n = int(input())

max_num = n // 3

remainder = n % 3

if(remainder == 0):
    print(max_num * 7)
elif(remainder == 1):
    print((max_num - 1) * 7 + 4)
elif(remainder == 2):
    print(max_num * 7 + 1)
    

# Số    : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Số ống: [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# Với 7 ống ta có thể tạo số 8 nhưng cũng có thể tạo ra được 1 số 7 và 1 số 4 (7 + 4 = 11) cho kết quả lớn hơn.
# Với 6 ống ta có thể tạo số 9 nhưng cũng có thể tạo ra được 2 số 7 (7 + 7 = 14) cho kết quả lớn hơn.
# Với 5 ống ta có thể tạo số 5 (Vì 5 lớn hơn 2 3 nên mặc định 5 ống ta sẽ chọn 5) nhưng cũng có thể tạo ra được 1 số 7 và 1 số 1 (7 + 1 = 8) cho kết quả lớn hơn.
# Với 4 ống ta chỉ có thể tạo ra số 4.
# Với 3 ống ta chỉ có thể tạo ra số 7.
# Với 2 ống ta chỉ có thể tạo ra số 1.

# => Nếu n % 3 = 0 -> max_num = (n // 3) * 7
#        n % 3 = 1 -> max_num = ((n // 3) - 1) * 7 + 4
#        n % 3 = 2 -> max_num = (n // 3) * 7 + 1