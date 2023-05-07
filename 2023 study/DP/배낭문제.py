capacity = 10
cntThings = 4
things = [[], [5, 10], [4,40], [6,30], [3,50]] # 물건 가치와 무게 
table = [ [0] * (capacity+1) for i in range(cntThings+1)] # DP기록 테이블

print('-------------------------------------------')
print('\t   <DP 배낭 알고리즘 START>')

for i in range(cntThings):#배낭 용량 0인 경우 K[물건, 0] = 0
    table[i][0] = 0
for w in range(0,capacity):#물건 고려X
    table[0][w] = 0

for i in range(1,cntThings+1):
    print('-------------------------------------------')
    if(i==1): print('\t   <물건', i, '만을 고려>')
    else: print('\t   <물건', i, '를 추가로 고려>')

    for w in range(1,capacity+1):# 임시 용량 : 1 ~ 10
        if(things[i][0] > w):# 물건 담기 X -> 이 전에 계산한 값이 일단은 최선임
            table[i][w] = table[i-1][w]
            print(f"배낭{w}kg : 물건{i}({things[i][0]}kg)담기 불가(이전 최적값 {table[i-1][w]}사용)")
        else:# 물건 담기 가능 -> 담지 않은 경우(이 전 계산값) Vs 담는 경우(갱신값)
            print(f"배낭{w}kg : 물건{i}({things[i][0]}kg)담기 가능(최적 경우 탐색) -> ", end ='')
            print(f"{table[i-1][w]} VS {table[i-1][w-things[i][0]]+things[i][1]} = ", end ="")
            table[i][w] = max(table[i-1][w], table[i-1][w-things[i][0]]+things[i][1])
            print(max(table[i-1][w], table[i-1][w-things[i][0]]+things[i][1]))
            # 이때까지 계산한 최적의 값  vs 이 전 배낭을 빼고 지금 걸 담는 값
            
print('-------------------------------------------')
print("\t  최종 테이블")
for i in range(1,cntThings+1):
    print('물건',i,': ', end='')
    for j in range(0, capacity):
        print(table[i][j], end=' ')
    print()
print('-------------------------------------------')

print("\t  최적해 :", table[4][10])
print('-------------------------------------------')