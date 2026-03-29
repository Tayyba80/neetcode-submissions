class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookupMap = {}
        for i , n in enumerate(nums):
            req = target - n
            if req in lookupMap:
                return [lookupMap[req],i]
            lookupMap[n] = i
            
        