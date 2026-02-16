class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for num in digits:
            ans=ans*10+num
        ans=ans+1
        result=[]
        ans=str(ans)
        for ch in ans:
            result.append(int(ch))
        return result