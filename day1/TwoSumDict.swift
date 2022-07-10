func twoSumWithDictionary(nums: [Int], target: Int) -> [Int] {
    var targetDictionary = [Int: Int]()

    for index in 0...nums.count {
        if let result = targetDictionary[target - nums[index]] {
            return [result, index]
        } else {
            targetDictionary[nums[index]] = index
        }
    }
    return []
}

print("TwoSunDictionary Test Started")
twoSumWithDictionary(nums: testList, target: testTarget)