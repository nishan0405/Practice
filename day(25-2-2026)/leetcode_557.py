class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        for i in range(len(a)):
            word=a[i]
            word=word[::-1]
            a[i]=word
        return " ".join(a)
