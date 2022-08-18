class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(list(s))
        for i,each in enumerate(s):
            if freq[each] == 1:
                return i
        return -1
