class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(1, len(points)):
            first = points[i-1]
            second = points[i]
            left = second[0] -first[0]
            right = second[1] -first[1]
            count += max(abs(left), abs(right))
                        
        return count
