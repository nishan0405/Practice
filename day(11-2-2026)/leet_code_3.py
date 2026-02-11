class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        max_len=0
        count=0
        for ch in s:
            if ch not in dic:
                dic[ch]=1
                count+=1
                max_len=max(max_len,count)
            elif ch in dic:
                del dic[ch]
                count=0
        return max_len