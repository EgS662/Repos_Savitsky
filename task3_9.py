class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, x):
    less_than_x = ListNode(None)
    greater_than_or_equal_x = ListNode(None)

    current_less = less_than_x
    current_greater = greater_than_or_equal_x

    while head:
        if head.val < x:
            current_less.next = head
            current_less = current_less.next
        else:
            current_greater.next = head
            current_greater = current_greater.next

        head = head.next

    current_greater.next = None
    current_less.next = greater_than_or_equal_x.next

    return less_than_x.next

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

partitioned_head = partition(node1, 3)

current = partitioned_head
while current:
    print(current.val)
    current = current.next