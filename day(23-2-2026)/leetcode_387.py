class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=defaultdict(int)
        st=''
        for ch in s:
            if ch not in a:
                a[ch]=1
            else:
                a[ch]=a[ch]+1
        for key,value in a.items():
            if value==1:
                st=key
                break
        if st == '':
            return -1
        return s.find(st)
                
        