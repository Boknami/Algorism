import sys
input=sys.stdin.readline

num = int(input())
ary = [[int(x) for x in input().split()] for y in range(num)]

blue = 0
white = 0

def division_conqu(x, y, n):
    base_color = ary[x][y]
    global blue
    global white
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(ary[i][j] != base_color):
                division_conqu(x,y,n//2)
                division_conqu(x,y + n//2,n//2)
                division_conqu(x+ n//2,y,n//2)
                division_conqu(x+ n//2,y + n//2,n//2)
                return 1
    if base_color == 0:
        white = white + 1
    else:
        blue = blue + 1
division_conqu(0,0, num)
print(white)
print(blue)
