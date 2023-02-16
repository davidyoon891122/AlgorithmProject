
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, value in enumerate(nums):
            print(i, value)
            if i % 2 == 0:
                sum += value
        
        return sum
            

nums_1 = [1,2,3,4]
s = Solution()
result = s.arrayPairSum(nums= nums_1)
print("result: {}".format(result))
