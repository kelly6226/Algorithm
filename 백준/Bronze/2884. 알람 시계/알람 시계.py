h, m = input().split()

hour = int(h) ### 시간
min = int(m) ### 분

### 현재 시간을 분으로 바꾸기
total = hour * 60 + min

### 현재 시간에서 45분을 빼기
final = total - 45

if (final > 0):
    finalH = int(final / 60)
    finalM = int(final % 60)
    print(finalH, finalM)
elif ((min - 45) > 0):
    finalM = min - 45
    print("0", finalM)
elif ((min-45) < 0):
    minusM = min - 45
    finalM = 60 + minusM
    print("23", finalM)
else:
    print("0 0")