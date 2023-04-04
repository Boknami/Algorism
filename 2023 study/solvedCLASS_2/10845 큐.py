import sys
input = sys.stdin.readline
n = int(input())
queue = []

for _ in range(n):
    cmd = input().split()

    if("push" in cmd):
        queue.append(cmd[1])
    elif("front" in cmd):
        if(queue):
            print(queue[0])
        else:
            print(-1)
    elif("size" in cmd): 
        print(len(queue))
    elif("pop" in cmd): 
        if(queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif("empty" in cmd): 
        if(queue):
            print(0)
        else:
            print(1)
    elif("back" in cmd): 
        if(queue):
            print(queue[-1])
        else:
            print(-1)
