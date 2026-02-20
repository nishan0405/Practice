class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[-1]
        b=nums[-2]
        c=nums[-3]
        s1=a*b*c
        s2=(nums[0]*nums[1]*nums[2])
        if s1>abs(s2):
            return s1
        else:
            return s2