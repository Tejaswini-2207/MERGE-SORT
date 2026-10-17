#Scenario: A platform receives several already-sorted linked lists and must combine them into one sorted linked list.


# Problem 5: Merge k Sorted Linked Lists
# Technique: Divide and Conquer

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(a, b):
    dummy = ListNode(0)
    tail = dummy

    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    # Attach the remaining nodes
    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return dummy.next


def merge_k_lists(lists):
    if not lists:
        return None

    # Repeatedly merge lists in pairs
    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            left = lists[i]

            if i + 1 < len(lists):
                right = lists[i + 1]
            else:
                right = None

            merged = merge_two_lists(left, right)
            merged_lists.append(merged)

        lists = merged_lists

    return lists[0]


def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    print(result)


# Test the program
input_lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

linked_lists = []

for values in input_lists:
    linked_lists.append(build_linked_list(values))

result = merge_k_lists(linked_lists)

print("Input:", input_lists)
print("Output:", end=" ")
print_linked_list(result)
