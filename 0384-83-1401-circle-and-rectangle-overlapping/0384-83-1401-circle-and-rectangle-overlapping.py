class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        x_nearest= max(x1, min(x2,xCenter))
        y_nearest= max(y1, min(y2,yCenter))

        dist_x= x_nearest - xCenter
        dist_y= y_nearest- yCenter

        return dist_x**2 + dist_y**2<= radius**2
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        