class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # index marking
        #array contains numbers in the range 1 to n, where n = len(nums) - 1 
        #so we can map n-1 as index of n

        for n in nums:
            index = abs(n) - 1 # as this line gives us index of same val same so when second same value come we'll jump to the index, as it is already marked we'll know that this num is duplicate
            if nums[index] < 0:
                return abs(n)
            nums[index] = nums[index] * -1
        return -1

        