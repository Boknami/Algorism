N = 1
while(N != 0):
    N = input()
    if(int(N)==0): break
    value = int(N)
    N_list = list(map(int, str(N)))

    if(100 <= value <= 999):
        if(N_list[0] == N_list[2]):
            print("yes")
        else:
            print("no")
    elif(10000 <= value <= 99999):
        if(N_list[0] == N_list[4] and N_list[1] == N_list[3]):
            print("yes")
        else:
            print("no")
    else:
        print("no")
