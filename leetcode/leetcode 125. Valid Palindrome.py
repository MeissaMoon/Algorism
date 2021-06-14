
[Input]
s =  "A man, a plan, a canal: Panama"
[Output] true

# 풀이 1
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

isPalindrome(s)
#pop()은 리스트에서 맨 마지막 요소를 출력하면서 그 요소를 리스트에서 삭제하는, 즉 리스트에서 꺼내버리는 함수.
#하나의 인자를 넣어주면 x위치에 있는 요소를 꺼내게 됨.
#pop(0)는 왼쪽부터 꺼냄

# 풀이 2
def isPalindrome(s):
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 풀이 3 
def isPalindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]