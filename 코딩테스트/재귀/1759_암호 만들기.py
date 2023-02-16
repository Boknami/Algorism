# 최소 한 개의 모음
# 최소 두 개의 자음
# 알파벳은 증가하는 순서
from itertools import combinations, permutations

comb ,number = map(int, input().split())
abc = []
abc = input().split()
combi = list(combinations(abc, 4))
combi.sort()

for i in range(len(combi)):
    aeiou = 0 
    etc = 0

    for j in range(comb):
        if(combi[i][j] == 'a' or combi[i][j]   == 'e' or combi[i][j]  == 'i' or combi[i][j]  == 'o' or combi[i][j]  == 'u'):
            aeiou += 1
        else:
            etc +=1
    
    if(aeiou < 1 or etc < 2):
        print(len(combi))
        print(combi.pop(i))
        print(len(combi))
    
print(combi)
#1 : 모든 경우에 수를 구하고 거기서 만족하는 거만 찾거나 불만족 빼기
#2 : 직접하나씩 조합
#3 : 모음 n개, 자음 m - n