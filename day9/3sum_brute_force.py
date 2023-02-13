
from typing import List

class Solution:
    def threeSum(self, nums: List[int]):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                print(i)
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    print(i,j)
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        print(i,j,k)
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()

result = s.threeSum(nums)

print(result)