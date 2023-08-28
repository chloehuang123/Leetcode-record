class MedianFinder:

    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        self.store.append(num)


    def findMedian(self) -> float:
        self.store.sort()
        length = len(self.store)
        if length % 2 == 0:
            return (self.store[length // 2 - 1] + self.store[length // 2]) / 2
        else:
            return self.store[length // 2]
        
