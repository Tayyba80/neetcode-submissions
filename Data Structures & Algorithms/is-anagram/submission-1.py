class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f=sorted(t)
        m=sorted(s)
        t=''.join(f)
        s=''.join(m)
        if(len(s)!=len(t)):
            return False    
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True