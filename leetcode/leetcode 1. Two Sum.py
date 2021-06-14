#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# 풀이 1 브루트 포스 : 정답을 찾을 때까지 무차별 대입
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): # i보다 커지면 stop
                if nums[i]+nums[j] == 9:
                    return [i,j]

# 풀이 2 정답에서 첫번째 값을 뺀 값이 있는지 비교  ----??????
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):   # i는 인덱스값, n은 값
            answer = target - n

        if answer in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(answer)+(i+1)

# 풀이 3 첫번째 수를 뺀 결과 키 조회
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} 

     # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

     # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:  # ??????
                return nums.index(num), nums_map[target - num]

# 풀이 4 조회 구조 개선
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
    # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
        nums_map[num] = i 


# 풀이 5 투 포인터 이용
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0 , len(nums) - 1
        print(right) # 3 
        while not left == right :
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] > target:
                left +=1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -=1
            else: 
                return left, right