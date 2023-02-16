
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        print(nums)
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

nums_1 = [1,2,3,4]
s = Solution()
result = s.arrayPairSum(nums= nums_1)
print("result: {}".format(result))
