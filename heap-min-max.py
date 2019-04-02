from heapq import heappush, heappop, heapify, nsmallest

class MinHeap:
    def __init__(self):
        self.heap = []

    def insertEl(self,el):
        heappush(self.heap,el)

    def getMin(self):
        return self.heap[0]

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertEl(self,el):
        heappush(self.heap,-el)

    def getMin(self):
        return -self.heap[0]

heapObj = MaxHeap()
heapObj.insertEl(3)
heapObj.insertEl(2)
heapObj.insertEl(15)
heapObj.insertEl(5)
heapObj.insertEl(4)
heapObj.insertEl(45)
