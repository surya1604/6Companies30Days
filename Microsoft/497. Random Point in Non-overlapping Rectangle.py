class Solution(object):

    def __init__(self, rects):
        self.rects = rects
        self.weights = []
        self.sum = 0

        for x1,y1,x2,y2 in self.rects:
            num_points= (x2 - x1 + 1)*( y2 - y1 + 1)
            self.weights.append(num_points)
            self.sum +=num_points
   

        self.weights=[x/self.sum for x in self.weights]

        """
        :type rects: List[List[int]]
        """

    def pick(self):
        ind=random.choices(range(len(self.rects)),self.weights)[0]
        x1,y1,x2,y2=self.rects[ind]
        return[random.randint(x1,x2),random.randint(y1,y2)]
    
        """
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
