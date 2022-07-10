from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# Test Case
print('TestCase Loop Solution')
test_list_one = [1,2,3,4]
test_target_one = 3
print(twoSum(test_list_one, test_target_one))


