class Solution(object):
    def isPalindrome(self, s):
        st=0
        e=len(s)-1
        while st<e:
            if not s[st].isalnum():
                st+=1
            elif not s[e].isalnum():
                e-=1
            elif s[st].lower()==s[e].lower():
                st+=1
                e-=1
            else:
                return False
        return True