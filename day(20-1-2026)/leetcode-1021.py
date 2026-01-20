class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        str2=""
        for i in range(len(s)):
            if s[i]=='(':
                if count>0:
                    str2+=s[i]
                count+=1

            elif s[i]==')':
                count-=1
                if count>0:
                    str2+=s[i]
        return str2
    
                