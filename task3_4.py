class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reorder_list(head):
    def find_middle(node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(node):
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    if not head or not head.next:
        return

    middle = find_middle(head)

    second_half = reverse_list(middle.next)
    middle.next = None

    first = head
    second = second_half

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

reorder_list(node1)

current = node1
while current:
    print(current.val)
    current = current.next