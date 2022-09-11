class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        def first(a):
            return a[0]
        
        performance = []
        for i, each in enumerate(speed):
            performance.append([each, efficiency[i]])
        
        performance.sort(reverse=True, key=first)
        
        mp = 0
        i, j = 0, k
        s = 0
        
        heap = []
        heapify(heap)
        
        for i in range(i, j):
            s += performance[i][0]
            heappush(heap, (performance[i][1],performance[i][0]))
            i += 1
        
        while j<n:
            m = heappop(heap)
            mp = max(mp, s*m[0])
            heappush(heap, (performance[j][1],performance[j][0]))
            s += performance[j][0] - m[1]
            j += 1
        m = heappop(heap)
        mp = max(mp, s*m[0])
        
        s -= m[1]
        while heap:
            m = heappop(heap)
            mp = max(mp, s*m[0])
            s -= m[1]
        
        return mp%1000000007
