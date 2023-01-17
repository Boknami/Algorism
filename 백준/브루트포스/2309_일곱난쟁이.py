ary = []

for i in range(9):
    ary.append(int(input()))

ary.sort()
sum = sum(ary)

for i in range(0, 8):
    for j in range(i+1, 9):
        if(sum - ary[i] - ary[j] == 100):
            exclu1 = ary[i]
            exclu2 = ary[j]
        
ary.remove(exclu1)
ary.remove(exclu2)

for i in range(len(ary)):
    print(ary[i])