class Solution(object):
    def imageSmoother(self, img):
        Rows, Col= len(img), len(img[0])

        res=[[0]*Col for _ in range(Rows)]

        for r in range(Rows):
            for c in range(Col):
                total, cnt= 0,0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if (i<0 or i==Rows) or (j<0 or j==Col):
                            continue
                        total+=img[i][j]
                        cnt+=1
                res[r][c]=total//cnt
        return res
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        
