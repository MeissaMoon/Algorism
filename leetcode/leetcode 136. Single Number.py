from collections import Counter 
from typing import List

class Solution: 
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = Counter(nums)  # counter 함수를 통해 숫자의 개수를 셉니다.
        items = count_dict.items()  # 키와 값을 가진 딕셔너리형태로 만들기 위해 .items()를 사용하여 넣었습니다.
        
        print(items)    # 출력해보면 dict_items([(2, 2), (1, 1)]) 

        for key, val in items: 
            if val == 1: answer = key # 값이 1개인 것을 찾아 리턴시킵니다. 
            break 
        return answer

    