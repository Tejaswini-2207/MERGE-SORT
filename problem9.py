#Count Inversions Using Merge Sort

def count_inversions(arr):
    def sort_count(a):
        if len(a) <= 1:
            return a, 0

        mid = len(a) // 2
        left, left_count = sort_count(a[:mid])
        right, right_count = sort_count(a[mid:])

        merged = []
        i = j = 0
        split_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                split_count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        total = left_count + right_count + split_count
        return merged, total

    return sort_count(arr)


arr = [2, 4, 1, 3, 5]

sorted_arr, inversions = count_inversions(arr)

print("Sorted array:", sorted_arr)
print("Inversions:", inversions)
