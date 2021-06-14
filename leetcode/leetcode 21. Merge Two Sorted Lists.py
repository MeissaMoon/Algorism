# 풀이 1
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return


# 풀이 2 미완성
"""
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    curr = dummy = ListNode()
    while l1 and l2 :
        if l1.val > l2.val:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next

        if not l1:
            curr.next = l2
        else:
            curr.next = l1

        return dummy
"""