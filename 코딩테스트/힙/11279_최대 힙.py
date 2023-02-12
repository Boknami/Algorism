import sys
import heapq

heap = []
n = int(input())

for i in range(n):
    k = int(sys.stdin.readline())

    if(k == 0):
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        #heapq는 최소힙을 기본으로 동작, 값을 음수로 만들어줘서 최대힙처럼 사용
        heapq.heappush(heap, (-k))
