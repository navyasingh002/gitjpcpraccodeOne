def sortKSortedArray(array, k):
    minHeapWithKElements = MinHeap(array[: min(k + 1, len(array))])
    nextIndexToInsertElement = 0
    for idx in range(k + 1, len(array)):
        minElement = minHeapwithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1

        currentElement = array[idx]
        minHeapwithKElements.insert(currentElement)

    while not minHeapWithkElements. isEmpty():
        minElement = minHeapwithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
    return array


class MinHeap:
    def _init_(self, array):
        self.heap = self.buildHeap(array)
    def isEmpty(self):
        return len(self. heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversedfrang((firstParentide + 1)):
             self.siftDown(currentIdx, len(array) - 1, array)
        return array

def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = currentIdx *2 +1
    while childOneIDx <= endIdx:
        childTwoIdx = currentIdx*2 +2 if currentIdx *2+2<=endIdx else -1
        if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToswap = childOneIdx
        if heap[idxToSwap]< heap[currentIdx]:
            self.swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToswap
            childOneIdx = currentIdx*2+1
        else:
            return

def siftUp(self, currentIdx, heap):
    parentIdx = (currentIdx -1)//2
    while currentIdx >0 and heap[currentIdx]<heap[parentIdx]:
        self.swap(currentIdx, parentIdx, heap)
        currentIdx =parentIdx
        parentIdx = (currentIdx -1)//2
def peak(self):
    return self.heap[0]

def remove(self):
    self.swap(0, len(self.heap)-1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap)1,self.heap)
    return valueToRemove
def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap)-1,self.heap)

def swap(self, i,j,heap):
    heap[i],heap[j]= heap[j],heap[i]