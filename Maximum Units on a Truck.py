class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def second(arr):
            return arr[1]
        
        boxTypes.sort(reverse = True, key=second)
        
        c = i = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] >= truckSize:
                c += truckSize*boxTypes[i][1]
            else:
                c += boxTypes[i][0]*boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        
        return c
