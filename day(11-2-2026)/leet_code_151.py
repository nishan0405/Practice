class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        s=" ".join(words)
        return s