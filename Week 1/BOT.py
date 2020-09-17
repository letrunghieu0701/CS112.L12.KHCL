def maxSubArray(arr, size):
    max_ending_here = arr[0]
    max_sub_arr = float('-inf')
    start = 0
    end = 0
    temp = 0

    for i in range(1,size):
        max_ending_here += arr[i]
        
        if max_ending_here > max_sub_arr:
            max_sub_arr = max_ending_here
            end = i
            start = temp
        
        elif max_ending_here < 0:
            max_ending_here = 0
            temp = i + 1
    
    print(start + 1, end + 1, max_sub_arr)

n = int(input())
arr = list(map(int, input().split()))
maxSubArray(arr,len(arr))
            
