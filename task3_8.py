class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_k_group(head, k):
    def reverse_group(node, k):
        prev = None
        current = node
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev, node

    dummy = ListNode(None)
    dummy.next = head
    prev_group_end = dummy

    while True:
        group_start = prev_group_end.next
        group_end = group_start

        for _ in range(k-1):
            if not group_end:
                return dummy.next
            group_end = group_end.next

        if not group_end:
            return dummy.next

        next_group_start = group_end.next
        group_end.next = None

        prev_group_end.next, new_group_start = reverse_group(group_start, k)
        new_group_start.next = next_group_start
        prev_group_end = new_group_start

    return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

reversed_head = reverse_k_group(node1, 2)

current = reversed_head
while current:
    print(current.val)
    current = current.next