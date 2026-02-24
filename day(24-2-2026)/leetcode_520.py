class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n <= 1:
            return True
        if all('A' <= ch <= 'Z' for ch in word):
            return True
        if all('a' <= ch <= 'z' for ch in word):
            return True
        if 'A' <= word[0] <= 'Z' and all('a' <= ch <= 'z' for ch in word[1:]):
            return True
        return False