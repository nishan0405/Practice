class Solution:
    def get_value(self, a):
        if a == 'I':
            return 1
        elif a == 'V':
            return 5
        elif a == 'X':
            return 10
        elif a == 'L':
            return 50
        elif a == 'C':
            return 100
        elif a == 'D':
            return 500
        elif a == 'M':
            return 1000

    def romanToInt(self, s: str) -> int:
        prev = 0
        roman = self.get_value(s[0])
        for i in range(1, len(s)):
            prev = self.get_value(s[i - 1])
            b = self.get_value(s[i])
            if prev < b:
                roman += b - 2 * prev
            else:
                roman += b
        return roman

        
        

           




      