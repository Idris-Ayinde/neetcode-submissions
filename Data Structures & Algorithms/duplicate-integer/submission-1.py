class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if ((i != j) and (nums[i] == nums[j])):
        #             return True
        # return False

        hashmap = {}
        for ele in nums:
            if ele not in hashmap:
                hashmap[ele] = True
            else:
                return True
        return False # No duplicate found

'''
Using in dictionary:
check if the key exist in the dictionary:
if this doesn't add
if it does: means the current ele is a duplicate: return false
'''