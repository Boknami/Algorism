# 피보나치 수열을 만들자
a = int(input())
result = 1

if(a == 1):
    result = 1
elif(a == 2):
    result = 1

b = result
c = result

if(a >= 3):
    for i in range(a-2):
        result = b + c
        b = c
        c = result
    
print(result)
print(result%1000000)