import random

def partition(arr, start, stop, pivot_ix):
    
    left = []
    pivot_count = 0
    right = []
    pivot = arr[pivot_ix]
    for ix in range(start, stop):
        if arr[ix] < pivot:
            left.append(arr[ix])
        elif arr[ix] == pivot:
            pivot_count += 1
        else:
            right.append(arr[ix])
    ix = start
    for x in left:
        arr[ix] = x
        ix += 1
    for i in range(pivot_count):
        arr[ix] = pivot
        ix += 1
    for x in right:
        arr[ix] = x
        ix += 1
    return start + len(left)

def quickselect(arr, k, start, stop):
    
    pivot_idx = random.randrange(start, stop)
    pivot_idx = partition(arr, start, stop, pivot_idx)
    pivot_order = pivot_idx + 1
    
    if pivot_order == k:
        return arr[pivot_idx]
    elif pivot_order < k:
        return quickselect(arr, k, pivot_idx + 1, stop)
    else:
        return quickselect(arr, k, 0, pivot_idx)

def absolute(value):
    return (value**2)**(0.5)

def knn_distance(arr,q,k):
    n = len(arr)
    difference = []
    orig_index = 0
    for num in arr:
        difference.append([abs(num-q), orig_index])
        orig_index += 1
    kth_info = quickselect(difference, k, 0, len(difference))
    distance = kth_info[0]
    kth_point = arr[kth_info[1]]
    return (distance, kth_point)
