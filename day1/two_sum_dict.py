from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    number_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in number_dict:
            return [number_dict[i], i]
        else:
            number_dict[nums[i]] = i

# TestCase
print('TestCase Loop Solution')
test_list_one = [1,2,3,4]
test_target_one = 3
print(twoSum(test_list_one, test_target_one))


