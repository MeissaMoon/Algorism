
def oddEvenList(self, head: ListNode) -> ListNode:
    # head  even_head
    # odd   even   odd2   even2
    # 1----> 2 ---> 3 ---> 4 ---> 5 ---> NULL
    if head is None:
        return None
    odd = head        # 시작점
    even = head.next  # 짝수는 1의 다음값
    even_head = even  # 짝수 2를 가리키는 포인터
    while even is not None and even.next is not None:
        odd.next = even.next  # 1의 next는 3이며, even값인 2의 다음값과 같다
        odd = odd.next        # 3이 새로운 odd가 됨
        even.next = odd.next  
        even = even.next      # 4가 새로운 even이 됨
    odd.next = even_head      # 홀수들 뒤에 짝수의 첫값이 오게 함
    return head