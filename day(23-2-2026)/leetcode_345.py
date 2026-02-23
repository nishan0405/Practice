class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) 
        i = 0
        j = len(s) - 1
        v = ['a', 'e', 'i', 'o', 'u']
        while i <= j:
            if s[i].lower() in v and s[j].lower() in v:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            else:
                if s[i].lower() not in v:
                    i += 1
                if s[j].lower() not in v:
                    j -= 1 
        return "".join(s)