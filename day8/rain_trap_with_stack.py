# LeetCode 42 Hard


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                print("waters: {}".format(waters))
                volume += distance * waters
                print("volume: {}".format(volume))
            stack.append(i)
            print(stack)
        return volume


trap = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
result = s.trap(height=trap)
print(result)