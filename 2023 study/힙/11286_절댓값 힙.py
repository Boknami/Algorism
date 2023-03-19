import sys
import heapq

class Num:
    def __self__(self, value):
        if(value < 0):
            self.value = -value
            self.sign = 1
        else:
            self.value = value
            self.sign = 0
