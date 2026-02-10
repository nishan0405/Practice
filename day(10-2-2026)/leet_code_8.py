class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        number=0
        neg=False
        if s.startswith('-'):
            neg=True
        if s.startswith('0'):
            return 0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            if ch.isalpha():
                break
        if neg:
            number=-1*number
        return number

            
        