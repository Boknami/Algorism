mi, ma = map(int, input().split())

sq = [4]

while(max(sq) < ma):
    num = 2
    sav = num * num
    sq.append(sav)
    num = num + 1

    print('--------------')
    print(mi, ma)
    print(num, sq)
