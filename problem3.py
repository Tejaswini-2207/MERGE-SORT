#Scenario: A music application stores song durations in a singly linked list. Sort the list using Merge Sort without converting it into an array.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists(a, b):
    dummy = ListNode()
    tail = dummy

    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    tail.next = a if a else b

    return dummy.next


def sort_list(head):
    if head is None or head.next is None:
        return head

    # Find the middle and split the list
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None

    left = sort_list(head)
    right = sort_list(slow)

    return merge_lists(left, right)


def build_list(values):
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def print_list(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


head = build_list([4, 2, 1, 3])

print("Original list:")
print_list(head)

sorted_head = sort_list(head)

print("Sorted list:")
print_list(sorted_head)
