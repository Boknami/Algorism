scale = list(map(int, input().split()))
not_as = 0
not_des = 0
not_mix = 0

for idx in range(7):
    if(scale[idx] > scale[idx+1]):
        break
    if(idx == 6):
        print('ascending')
        exit()

for idx in range(7):
    if(scale[idx] < scale[idx+1]):
        break
    if(idx == 6):
        print('descending')
        exit()
print("mixed")