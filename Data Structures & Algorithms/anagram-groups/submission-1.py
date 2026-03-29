class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sortedV = ''.join(sorted(i))
            result[sortedV].append(i)
        return list(result.values())
        