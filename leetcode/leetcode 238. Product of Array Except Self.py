Input:  [1,2,3,4]
Output: [24,12,8,6]
# 나눗셈을 하지않고 O(n)풀이하라!
from typing import List
# 풀이 1 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

def productExceptSelf(self, nums: List[int]) -> List[int]:
    out = []
    p = 1 

    # 왼쪽 곱셈
    for i in range(0, lens(nums)):
        out.append(p)
        p= p*nums[i]
    p=1

    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0-1, -1):
        out[i] = out[i] *p
        p = p*nums[i]
    return out