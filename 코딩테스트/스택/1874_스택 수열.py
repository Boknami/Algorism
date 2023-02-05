stack = []
ans = []
n = int(input())
cur = 1
f = 0

for i in range(n):
    find = int(input())
    
    # push
    while cur <= find:
            stack.append(cur)
            ans.append('+')
            cur += 1
    # pop
    if(stack[-1] == find):
        stack.pop()
        ans.append('-')
        if(i == n- 1):
            for j in range(len(ans)): print(ans[j])
        
    else:
        print("NO")
        break

