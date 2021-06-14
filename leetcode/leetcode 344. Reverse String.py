[Input] s = ["h","e","l","l","o"]
[Output]  ["o","l","l","e","h"]

from typing import List
def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left] # 파이썬은 이런게 되다니 놀랍
        left += 1
        right -= 1

reverseString(s)
print(s)

def reverseString(s: List[str]) -> None:
    s.reverse()