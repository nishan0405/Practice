from typing import List
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        counts = Counter()
        for word in words:
            if word not in banned_set:
                counts[word] += 1
        return counts.most_common(1)[0][0]