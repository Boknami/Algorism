import sys
n = int(sys.stdin.readline())

stack = []

case = n

for i in range(case):
    com = sys.stdin.readline().split()

    if(com[0] == 'push'):
        stack.append(com[1])
    elif com[0] == 'pop':
        if(len(stack) == 0):
            print('-1')
            continue
        print(stack.pop(len(stack) - 1))
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if(len(stack) > 0):
            print('0')
        elif(len(stack) == 0):
            print('1')
    elif com[0] == 'top':
        if(len(stack) == 0):
            print('-1')
        elif(len(stack) != 0):
            print(stack[len(stack) - 1])
