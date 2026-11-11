class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1
        
        while lower_bound <= upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            if target > nums[midpoint]:
                lower_bound = midpoint + 1
            elif target < nums[midpoint]:
                upper_bound = midpoint - 1
            else:
                return midpoint
        return -1
