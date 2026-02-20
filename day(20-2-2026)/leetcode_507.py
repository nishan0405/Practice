class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans=[]
        for i in range(1,(num//2)+1):
            if num%i==0:
                ans.append(i)
        s=sum(ans)
        return s==num
        