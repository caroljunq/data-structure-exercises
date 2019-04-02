def binSearch(arr,min_index,max_index,val):

    middle = round((max_index + min_index)/2)

    if max_index >= min_index:
        if arr[middle] == val:
            return middle

        elif arr[middle] > val:
            return binSearch(arr, min_index, middle-1, val)

        else:
            return binSearch(arr, middle + 1, max_index, val)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 3

# Function call
result = binSearch(arr, 0, len(arr)-1, x)

print(result)
