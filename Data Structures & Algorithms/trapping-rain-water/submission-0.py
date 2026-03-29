class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = [0] * length
        right = [0] * length

        left[0] = height[0]
        right[length - 1] = height[length - 1]

        for i in range(1, length):
            left[i] = max(left[i - 1], height[i])
        
        for i in range(length - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        water_trapped = 0
        for i in range(length):
            water_trapped += min(left[i], right[i]) - height[i]
        
        return water_trapped
        