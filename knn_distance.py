def knn_distance(arr,q,k):
    n = len(arr)
    difference = []
    orig_index = 0
    for num in arr:
        difference.append([np.abs(num-q), orig_index])
        orig_index += 1
    difference = sorted(difference)

    return (difference[k-1][0], arr[difference[k-1][1]])
