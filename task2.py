class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    second_node = head.next
    head.next = swap_pairs(second_node.next)
    second_node.next = head
    return second_node

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

new_head = swap_pairs(head)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
