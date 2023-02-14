b1 = []
b2 = []
b3 = []
res = []
cnt = 0

def hanoi():  
    if(b3 == res):
        return
    
    getB = b1.pop()
    if(b2[len] == 0 or b2[len(b2)-1] > getB):
        b2.append(getB)
    elif(b3[len] == 0 or b3[len(b3)-1] > getB):
        b2.append(getB)
    else:
        

    # b2.append(b1.pop()) #조건(비거나 이미 차있는거중에 넣을 수 있는 상태거나)
    # b3.append(b1.pop())
    # b3.append(b2.pop())
    # b2.append(b1.pop())

    # #밑에꺼 뺴면된다 옮기자
    # b3.pop()



    # if(b1[0] == value or b2[0] == value):
    #     if(b3[find] == value+1 or len(b3) == 0):
            

board = int(input())

for i in range(0, board + 1, 1):
    b1.append(i)

res = b1