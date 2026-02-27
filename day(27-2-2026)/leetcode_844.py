class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = [], []
        a.extend(s)
        b.extend(t)
        i = 0
        while i < len(a):
            if a[i] == '#':
                a.pop(i)
                if i > 0:
                    a.pop(i - 1)
                    i -= 1
            else:
                i += 1
        i = 0
        while i < len(b):
            if b[i] == '#':
                b.pop(i)
                if i > 0:
                    b.pop(i - 1)
                    i -= 1
            else:
                i += 1
        return ''.join(a) == ''.join(b)