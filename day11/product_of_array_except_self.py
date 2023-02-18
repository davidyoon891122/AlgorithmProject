
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # left product
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        print(out)
        p = 1
        # plus right value
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
            print("out: {}, p: {}".format(out[i], p))
        return out 
        
            

nums_1 = [1,2,3,4]
s = Solution()
result = s.productExceptSelf(nums= nums_1)
print("result: {}".format(result))
