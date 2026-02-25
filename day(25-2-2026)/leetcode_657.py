class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l_count=0
        r_count=0
        u_count=0
        d_count=0
        for ch in moves:
            if ch=='L':
                l_count+=1
            elif ch=='R':
                r_count+=1
            elif ch=='U':
                u_count+=1
            else:
                d_count+=1
        if l_count==r_count and u_count==d_count:
            return True
        return False