import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = input()

cnt = 0
testN = (N * 2) + 1
find_st = []
find_st.append('I')
for i in range(N):
    find_st.append('O')
    find_st.append('I')

for j in range(M - testN):
    if(S[j] == find_st[0]):
        for k in range(1, testN, 1):
            if (S[j + k] == find_st[k]):
                if(k == testN-1):
                    cnt += 1
            else:
                break

print(cnt)
