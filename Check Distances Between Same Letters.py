class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        for i,each in enumerate(s):
            if each in d:
                dist = i-d[each]-1
                pos = ord(each) - ord('a')
                if distance[pos] != dist:
                    return False
            else:
                d[each] = i
        return True
