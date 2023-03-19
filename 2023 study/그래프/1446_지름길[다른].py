class Road:
    def __self__(self, start, end, leng):
        self.start = start
        self.end = end
        self.leng = leng
        self.efficiency = end-start-leng

road_num, km = map(int, input().split())

cur = 0
dis = 0
RoadList = []

for i in range(n):
    start, end, leng = map(int, input().split())

    if(leng > end-start or end > d or start < cur):
        continue
    RoadList.append(Road(start, end, leng))
    
