#Scenario: A bank has thousands of transaction amounts that must be sorted. The algorithm must guarantee \(O(n\log n)\) worst-case time.

def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = low + (high - low) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, mid, high)


transactions = [5000, 1200, 8500, 300, 4200, 1000]

merge_sort(transactions, 0, len(transactions) - 1)

print("Sorted transactions:", transactions)
