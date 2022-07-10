func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    for index in 0...nums.count {
        for nextIndex in 1...nums.count {
            if nums[index] + nums[nextIndex] == target {
                return [index, nextIndex]
            }
        }
    }
    return []
}