class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict=dict(Counter(s))
        tdict=dict(Counter(t))
        if sdict == tdict:
            return True
        else:
            return False
        