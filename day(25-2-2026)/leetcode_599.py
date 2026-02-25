class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        best = float('inf')
        for word in list1:
            if word in list2:
                total = list1.index(word) + list2.index(word)

                if total < best:
                    best = total
                    ans = [word]
                elif total == best:
                    ans.append(word)
        return ans