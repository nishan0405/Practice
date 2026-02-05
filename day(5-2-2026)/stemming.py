class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=strs[0]
        res=""
        b=strs[-1]
        c=min(len(a),len(b))
        for i in range(c):
            if a[i]!=b[i]:
                break
            else:
                res+=a[i]
        return res
        