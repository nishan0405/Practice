class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=0
        b=0
        for ch in t:
            a+=ord(ch)
        for ch in s:
            b+=ord(ch)
        return chr(a-b)
        