class Solution:
    def climbStairs(self, n: int) -> int:
        n1=0
        n2=1
        ans=0
        for i in range(n):
            if n<1:
                return 1
            ans=n1+n2
            n1=n2
            n2=ans
        return ans