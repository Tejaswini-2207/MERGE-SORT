#Scenario: A system analyzes how far an array is from being sorted. An inversion is a pair of positions \(i<j\) where \(A[i]>A[j]\).

def count_inversions(arr):
    def sort_count(a):
        if len(a) <= 1:
            return a, 0

        mid = len(a) // 2

        left, count_left = sort_count(a[:mid])
        right, count_right = sort_count(a[mid:])

        merged = []
        i = j = 0
        count_split = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count_split += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        total = count_left + count_right + count_split
        return merged, total

    return sort_count(arr)


arr = [5, 3, 2, 4, 1]

sorted_arr, total = count_inversions(arr)

print("Sorted array:", sorted_arr)
print("Inversions:", total)
