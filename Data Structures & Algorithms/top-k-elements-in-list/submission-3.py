class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)
        topk = [num for cnt,num in arr[:k]]
        return topk
        