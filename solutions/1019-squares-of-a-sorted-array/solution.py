class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1

        result = [0] * len(nums) #[0,0,0,0,0]
        position = len(nums) - 1 #This tells us where to put the next largest square.

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] ** 2
                left += 1
            else:
                result[position] = nums[right] ** 2
                right -= 1

            position -= 1

        return result
