class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        n=len(a)
        if n%2!=0:
            b=int(n/2+0.5)-1
            return float(a[b])
        else:
            c=int(n/2)-1
            d=(a[c]+a[c+1])/2
            return d