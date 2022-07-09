# 생각보다 시간이 걸림
# 모든 경우의 숫자를 구하는데 식을 어떻게 세울지..
Card, Max = map(int, input().split())
Ary = list(map(int, input().split()))

Add = 0
save = 0

for i in range(0, Card):
    for j in range(i+1, Card):
        for k in range(j+1 , Card):
            Add = Ary[i] + Ary[j] + Ary[k]

            if(Add <= Max):
                save = max(Add, save)
print(save)