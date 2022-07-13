import sys
input=sys.stdin.readline

Stack = []

def push(k):
    Stack.append(k)

def pop():
    if(len(Stack) == 0):
        print('-1')
    else:
        popping = Stack.pop()
        print(popping)

def size():
    print(len(Stack))

def empty():
    if(len(Stack) == 0):
        print('1')
    else:
        print('0')

def top():
    if(len(Stack) == 0):
        print('-1')
    else:
        print(Stack[-1])
    
#명령어 개수
N = int(input())

#명령어 입력 받고 처리
for i in range(0, N):
    command = input()

    if("push" in command):
        a, b = command.split()
        push(int(b))

    elif("pop" in command):
        pop()
    
    elif("size" in command):
        size()

    elif("empty" in command):
        empty()

    elif("top" in command):
        top()
