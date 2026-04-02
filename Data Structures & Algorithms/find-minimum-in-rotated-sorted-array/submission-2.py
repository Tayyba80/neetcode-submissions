class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r: # we use l<r condition when we have to search the boundary and we use l<= r condition when we are searching exact value
            m = l + ((r-l)//2)
            if nums[m] <= nums[r]:
                r = m # we can't do m-1 this can skip the answer 
            else:
                l = m + 1
        return nums[r]



        