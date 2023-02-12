import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())

    if(m == 0):
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(m), m))