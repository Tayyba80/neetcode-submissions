class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 , max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2 # // gives floor as ans like 2.63 if res of divison it will ans 2
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i / k) # / gives floated ans fill 2.63
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
