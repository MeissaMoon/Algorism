# 풀이 1 재귀구조
def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev                      # 맨처음 리턴된 prev는 뒤집힌 연결리스트의 첫번째 노드가 됨
            next, node.next = node.next, prev    # 다음노드 next를 계속 다음 값으로 지정해주면서 node.next는 prev와 계속 리스트를 연결 
            return reverse(next, node)           

        return reverse(head)

# 풀이 2 반복구조
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None     # node가 None이 되고 뒤집힌 prev가 첫번째 값 head가 될때 종료
    while node:
        next, node.next = node.next, prev   # node의 다음값과 이전 값을 비교하면서 뒤집는다?
        prev, node = node, next
    return prev

# 풀이 3
def reverseList(self, head: ListNode) -> ListNode:
    prev = None    # Singly Linked list라 만들어줌
    curr = head

    while curr != None:    # 마지막 값이 None이 아닐때까지
        tmp = curr.next
        curr.next = prev   # 2가 1을 가리키게
        prev = curr        # 3을 2로 가리키게
        curr = tmp         # 2가 3으로 
    return prev
