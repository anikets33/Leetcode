class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows-1):
            temp = [1]
            for j in range(1, len(res[-1])):
                temp.append(res[-1][j-1] + res[-1][j])
            temp.append(1)
            res.append(temp)
        return res
