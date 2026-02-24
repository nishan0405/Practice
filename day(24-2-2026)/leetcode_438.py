class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i=0
        j=len(p)
        p=sorted(p)
        ans=[]
        while j<=len(s):
            a=sorted(s[i:j])
            if a==p:
                ans.append(i)
            i+=1
            j+=1
        return ans