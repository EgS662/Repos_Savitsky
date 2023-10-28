class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next


head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)

result1 = remove_duplicates(head1)
print_list(result1)