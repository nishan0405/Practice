class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dis={}
        res=[]
        for i in range(len(nums)):
            dis[nums[i]]=i
        for i in range(len(nums)):
            a=target-nums[i]
            if a in dis and dis[a] != i:
                res.append(i)
                res.append(dis[a])
                break
        return res
