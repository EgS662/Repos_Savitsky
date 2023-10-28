class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def double_number(head):
    def convert_to_number(node):
        result = 0
        while node:
            result = result * 10 + node.val
            node = node.next
        return result

    def convert_to_list(number):
        if number == 0:
            return ListNode(0)
        
        dummy = ListNode(None)
        current = dummy
        while number > 0:
            current.next = ListNode(number % 10)
            current = current.next
            number //= 10
        return dummy.next

    num = convert_to_number(head)
    doubled_num = num * 2
    return convert_to_list(doubled_num)

node1 = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(9)

node1.next = node2
node2.next = node3

result_head = double_number(node1)

current = result_head
while current:
    print(current.val)
    current = current.next