Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.


# 풀이 1 오름차순 풀이
def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0 
        pair = []
        nums.sort()
   

        for n in nums:
            # 앞에서 부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
            
        return sum


# 풀이 2 짝수번째 값 계산
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째의 합 계산
        if i%2 == 0 :
            sum += n

    return sum


# 풀이 3 파이썬다운 방식
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])     # 분류된 nums를 [::2] = 2칸씩 건너뛴다
