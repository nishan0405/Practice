class Solution:
    def checkRecord(self, s: str) -> bool:
        l_count=0
        eligible=True
        a_count=0
        for ch in s:
            if ch=='L':
                l_count+=1
                if l_count>=3:
                    eligible=False
                    break
            elif ch=='A':
                l_count=0
                a_count+=1
                if a_count>=2:
                    eligible=False
                    break
            else:
                l_count=0
        return eligible