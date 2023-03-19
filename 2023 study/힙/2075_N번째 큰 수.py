import sys
import heapq

heap = []
n = int(input())

for i in range(n):
    k = list(map(int, input().split()))
    
    if(heap):
        for j in k:
            if(heap[0] < j):
                heapq.heappop(heap)
                heapq.heappush(heap, j)
    else:
        for j in k:
            heapq.heappush(heap, j)
                    
print(heapq.heappop(heap))