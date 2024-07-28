h, m = input().split()
requireMin = int(input()) ### 필요한 시간 (분 단위)

hour = int(h) ### 현재 시
min = int(m) ### 현재 분

total = hour * 60 + min + requireMin

totalH = int(total / 60)
totalM = int(total % 60)

if totalH > 23:
    finalH = totalH - 24
    print(finalH, totalM)
else:
    print(totalH, totalM)