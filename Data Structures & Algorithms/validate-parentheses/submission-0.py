class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]==')' or s[0]=='}' or s[0]==']':
            return False
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif (stack[-1]=='(' and s[i]==')') or (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') :
                stack.pop()
            else:
                stack.append(s[i])
        if(len(stack)==0):
            return True
        return False

        