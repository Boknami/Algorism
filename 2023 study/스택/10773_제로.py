k = int(input())
money = []

for i in range(k):
    talk = int(input())

    if(talk == 0):
        money.pop()
    else:
        money.append(talk)

print(sum(money))