class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)/2
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key,value in freq.items():
            if value>=n:
                return key

        


        