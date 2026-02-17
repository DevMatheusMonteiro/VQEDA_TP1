class BubbleSort:
    def __init__(self, array):
        self.__a = array
        self.__nItems = len(array)

    @property
    def array(self):
        return self.__a
    @property
    def nItems(self):
        return self.__nItems

    def swap(self, i, j):
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def bubbleSort(self):
        left = 0
        right = self.__nItems - 1

        while left < right:
            for i in range(left, right):
                if self.__a[i] > self.__a[i+1]:
                    self.swap(i, i+1)
            right -= 1

            for i in range(right, left, -1):
                if self.__a[i] < self.__a[i-1]:
                    self.swap(i, i-1)
            left += 1

bubbleSort = BubbleSort([64, 34, 25, 12, 22, 11, 90])
print(bubbleSort.array)
bubbleSort.bubbleSort()
print(bubbleSort.array)