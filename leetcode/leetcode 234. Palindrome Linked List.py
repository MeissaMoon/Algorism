Input: 1->2 -> 2 -> 1
Output: false


def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q = collections.deque()

    if not head:      # head가 비어있다면 True
        return True

    node = head       # 임시 변수를 설정해줘야 포인터를 찾아서 할 수 있음

    while node is not None:
        q.append(node.val)  # 노드 값 추가
        node = node.next    # 그 다음 노드를 받아옴

    while len(q) > 1:       # 2개를 뽑아야하기때문
        if q.popleft() != q.pop():     # 맨 앞과 맨 뒤가 같지 않다면 
            return False

    return True