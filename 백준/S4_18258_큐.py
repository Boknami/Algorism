import sys
input=sys.stdin.readline
from collections import deque

que = deque()

for i in range(int(input())):
    command = input()

    if("push" in command):
        a, b = command.split()
        que.append(int(b))

    elif("pop" in command):
        if(len(que) == 0):
            print('-1')
        else:
            print(que.popleft())
    elif("size" in command):
        print(len(que))
    elif("empty" in command):
        if(len(que) == 0):
            print('1')
        else:
            print('0')
    elif("front" in command):
        if(len(que) == 0):
            print('-1')
        else:
            print(que[0])
    elif("back" in command):
        if(len(que) == 0):
            print('-1')
        else:
            print(que[len(que) - 1])
    
