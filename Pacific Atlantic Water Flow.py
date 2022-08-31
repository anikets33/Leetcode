class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        #can use memoization for atlantic as well as pacific
        dpac = {}
        datl = {}
        
        def gotoAtlantic(i, j, vis):
            if i == len(heights)-1 or j == len(heights[0])-1:
                return True
            if (i,j) in vis:
                return False
            vis[(i,j)] = 1
            if (i,j) in datl:
                return datl[(i,j)]
            
            left, right, up, down = False, False, False, False
            if (j-1)>=0 and heights[i][j] >= heights[i][j-1]:
                left = gotoAtlantic(i, j-1, vis)
            if (j+1)<n and heights[i][j] >= heights[i][j+1]:
                right = gotoAtlantic(i, j+1, vis)
            if (i-1)>=0 and heights[i][j] >= heights[i-1][j]:
                up = gotoAtlantic(i-1, j, vis)
            if (i+1)<m and heights[i][j] >= heights[i+1][j]:
                down = gotoAtlantic(i+1, j, vis)
                
            boolean = left or right or up or down
            #datl[(i,j)] = boolean
            return boolean
        
        def gotoPacific(i, j, vis):
            if i == 0 or j == 0:
                return True
            if (i,j) in vis:
                return False
            vis[(i,j)] = 1
            if (i,j) in dpac:
                return dpac[(i,j)]
            
            left, right, up, down = False, False, False, False
            if (j-1)>=0 and heights[i][j] >= heights[i][j-1]:
                left = gotoPacific(i, j-1, vis)
            if (j+1)<n and heights[i][j] >= heights[i][j+1]:
                right = gotoPacific(i, j+1, vis)
            if (i-1)>=0 and heights[i][j] >= heights[i-1][j]:
                up = gotoPacific(i-1, j, vis)
            if (i+1)<m and heights[i][j] >= heights[i+1][j]:
                down = gotoPacific(i+1, j, vis)
                
            boolean = left or right or up or down
            #dpac[(i,j)] = boolean
            return boolean
                
        
        res = []
        
        for i in range(m):
            for j in range(n):
                #print(gotoAtlantic(i,j, {}))
                #print(gotoPacific(i,j, {}))
                a = gotoAtlantic(i,j, {})
                datl[(i,j)] = a
                b = gotoPacific(i,j, {})
                dpac[(i,j)] = b
                if a and b:
                    res.append([i, j])
        #print(dpac)
        return res
