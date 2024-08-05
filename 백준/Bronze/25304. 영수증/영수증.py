### 영수증에 적힌 총 금액
X = int(input())

### 영수증에 적힌 구매한 물건의 종류의 수
N = int(input())

### 총 실제 금액
total = 0

for i in range(0, N):
    price, amount = input().split()
    price = int(price)
    amount = int(amount)
    total = total + (price * amount)

if X == total:
    print("Yes")
else:
    print("No")