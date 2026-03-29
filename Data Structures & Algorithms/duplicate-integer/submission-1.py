from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = dict(Counter(nums))
        for c in maps.values():
            if c > 1:
                return True;
        return False

        

        