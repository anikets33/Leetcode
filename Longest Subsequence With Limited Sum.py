class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = list(accumulate(nums))
        res = []
        for each in queries:
            b = bisect.bisect(pre, each)
            res.append(b)
        return res
