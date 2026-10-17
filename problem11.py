#Sort a Linked 

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
        values.append(head.val)
        head = head.next

    print(" -> ".join(map(str, values)))


head = build_list([4, 2, 1, 3, 5])

print("Original list:")
print_list(head)

head = sort_list(head)

print("Sorted list:")
print_list(head)
