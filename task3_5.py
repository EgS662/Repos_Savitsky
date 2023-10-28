class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

delete_node(node2)

current = node1
while current:
    print(current.val)
    current = current.next