class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums= sorted(set(nums))
        curr = 1
        longest=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr +=1
            else:
                longest = max(longest,curr)
                curr = 1
        longest = max(longest,curr)
        return longest
        