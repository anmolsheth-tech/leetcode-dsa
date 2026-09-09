class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #2-pointer approach, i is the slow pointer
        i =0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for k in range(i, len(nums)):
            nums[k] = 0
        
        return nums



