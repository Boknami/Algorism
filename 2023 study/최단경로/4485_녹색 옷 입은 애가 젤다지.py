endValue = 0
while(True):
    cave_size = int(input())
    if(cave_size == endValue):break
    cave = []
    for i in range(cave_size):
        cave.append(list(map(int, input().split())))
    
    
