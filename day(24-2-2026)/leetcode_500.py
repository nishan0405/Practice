class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a='qwertyuiop'
        b='asdfghjkl'
        c='zxcvbnm'
        ans=[]
        for word in words:
            w=word.lower()
            if w[0] in a:
                row=a
            elif w[0] in b:
                row=b
            else:
                row=c
            ok=True
            for ch in w:
                if ch not in row:
                    ok=False
                    break
            if ok:
                ans.append(word)
        return ans



        