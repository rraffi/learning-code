def compress_array(arr, k):
    compressed = []
    i = 0
    while i < len(arr) - 1:
        if arr[i] * arr[i+1] <= k:
            compressed.append(arr[i] * arr[i+1])
            i = i + 2
        else:
            compressed.append(arr[i])
            i = i + 1
    
    if len(arr) % 2 == 1:
        compressed.append(arr[i])
    print(i)
    return len(compressed)


input_arr = [5,1,3,4]
print(compress_array(input_arr, 6))
            
