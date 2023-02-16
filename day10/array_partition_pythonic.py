
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums[::2]))
            

nums_1 = [1,2,3,4]
s = Solution()
result = s.arrayPairSum(nums= nums_1)
print("result: {}".format(result))
