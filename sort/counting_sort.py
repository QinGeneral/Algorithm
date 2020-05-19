def counting_sort(array):
    max = array[0]
    for i in array:
        if max < i:
            max = i
    max += 1
    
    count_array = [0] * max
    for i in array:
        count_array[i] += 1
    
    # 可以用下两行代替下边的 total count array
    # for i in range(1, len(count_array)):
        # count_array[i] += count_array[i - 1]
    
    total_count_array = [0] * max
    sum = 0
    index = 0
    for i in count_array:
        sum += i
        total_count_array[index] = sum
        index += 1
    
    print(count_array, total_count_array)

    result_array = [0] * len(array)
    for i in reversed(array):
        index = total_count_array[i] = total_count_array[i] - 1
        result_array[index] = i
        print(result_array)
    print(result_array)


counting_sort([2, 5, 3, 0, 2, 3, 0, 3])