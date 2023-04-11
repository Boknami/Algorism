import sys
input = sys.stdin.readline

n = int(input())
pList=[]

for idx in range (n): 
  age,name= map(str, input().split())
  pList.append([int(age), idx, name]) 

pList.sort()
for idx in range(n):
    print(f'{pList[idx][0]} {pList[idx][2]}')