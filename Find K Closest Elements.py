class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        t = []
        for i, each in enumerate(arr):
            t.append((abs(each - x), i))
        
        heapify(t)
        
        res = []
        while k>0:
            temp = heappop(t)
            res.append(arr[temp[1]])
            k -= 1
        
        res.sort()
        return res
