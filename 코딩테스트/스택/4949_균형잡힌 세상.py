while True:
    str = input()
    stack = []

    if(str == '.'):
        break

    f = 0

    for i in (str):

        # 괄호의 시작은 append
        if(i == '(' or i == '['):
            stack.append(i)
        # 끝나는 괄호는 짝이 맞는 경우 pop 아니면 append
        elif(i == ')'):
            if (len(stack) != 0 and stack[-1] == '(' ):
                stack.pop()
            else:
                print('no')
                f = 1
                break
        elif(i == ']'):
            if (len(stack) != 0 and stack[-1] == '['):
                stack.pop()
            else:
                print('no')
                f = 1
                break

    # 스택에 남은 게 있다(짝이 맞지 않는 게 존재)
    if(f == 0):
        if len(stack) == 0:
            print('yes')
        else:
            print('no')



