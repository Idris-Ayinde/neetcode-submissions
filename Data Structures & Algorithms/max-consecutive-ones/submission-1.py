class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
            elif nums[i] == 0:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0 # Zero rests the current count even if it didn't beat the max
        if current_count > max_count:
            return current_count
        return max_count
                
