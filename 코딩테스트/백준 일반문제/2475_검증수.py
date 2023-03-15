ary = list(map(int, input().split()))
certNum = 0

for aryVale in ary:
    certNum = certNum + aryVale*aryVale

print(certNum%10)