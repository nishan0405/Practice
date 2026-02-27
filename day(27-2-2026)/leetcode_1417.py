class Solution:
    def reformat(self, s: str) -> str:
        num = []
        digit = []
        
        for ch in s:
            if ch.isdigit():
                num.append(ch)
            else:
                digit.append(ch)
        
        if abs(len(num) - len(digit)) > 1:
            return ""
        
        res = []
        
        if len(num) > len(digit):
            first, second = num, digit
        else:
            first, second = digit, num
        
        for i in range(len(second)):
            res.append(first[i])
            res.append(second[i])
        
        if len(first) > len(second):
            res.append(first[-1])
        
        return "".join(res)