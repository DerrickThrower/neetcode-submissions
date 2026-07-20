class MedianFinder:

    def __init__(self):
        self.arrayL = []
        

    def addNum(self, num: int) -> None:
        self.arrayL.append(num)
        

        

    def findMedian(self) -> float:
        if not self.arrayL:
            raise ValueError("findMedian called with no numbers added")

        self.arrayL.sort()

        if len(self.arrayL) % 2 == 0:
            median =(self.arrayL[len(self.arrayL)//2] + self.arrayL[(len(self.arrayL)//2)-1]) / 2
            return median

            


        else:
            return self.arrayL[len(self.arrayL)//2]

            


        
        