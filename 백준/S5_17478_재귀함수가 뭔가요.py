repeat = int(input())
repeat = repeat + 1

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

for i in range(0, repeat):
    if(i == 0):
        print('"재귀함수가 뭔가요?"')
        print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    else:
        for a in range(0, i):
            print('____', end='')
        print('"재귀함수가 뭔가요?"')

        for b in range(0, i):
            print('____', end='')
        
        if i == (repeat-1):
            print('"재귀함수는 자기 자신을 호출하는 함수라네"')
            break

        print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')

        for c in range(0, i):
            print('____', end='')
        print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')

        for d in range(0, i):
            print('____', end='')
        print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

for i in range(repeat-1, -1, -1):
    for a in range(0, i):
        print('____', end='')
    print('라고 답변하였지.')