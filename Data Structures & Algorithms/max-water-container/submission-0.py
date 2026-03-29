class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0, len(heights)-1
        maxarea=0
        while left < right:
            curr=min(heights[left],heights[right])
            width=right-left
            area=width*curr
            maxarea=max(maxarea,area)
            if heights[left]>heights[right]:
                right -=1
            else: left+=1
        return maxarea
        