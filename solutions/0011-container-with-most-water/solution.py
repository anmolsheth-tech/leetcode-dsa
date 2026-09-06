#2 pointer problem
#Area of a rectangle = width * height
#Width = right - left
#shorter line is limiting the water height
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currentHeight = min(height[left], height[right])
            width = right - left
            area = currentHeight * width
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
