class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=int(num)
        res=""
        while n>0:
            a=n%10
            if(a%2!=0):
                res+=str(n)
                return res
            else:
                n=n//10
        return res

        