class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_lists(l1, l2):
    dummy = ListNode(None)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

def merge_k_sorted_lists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged = merge_two_lists(lists[i], lists[i+1])
                merged_lists.append(merged)
            else:
                merged_lists.append(lists[i])

        lists = merged_lists

    return lists[0]

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

merged_list = merge_k_sorted_lists([list1, list2, list3])

current = merged_list
while current:
    print(current.val)
    current = current.next