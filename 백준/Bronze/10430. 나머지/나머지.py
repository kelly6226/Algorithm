n1, n2, n3 = input().split()

num1 = int(n1)
num2 = int(n2)
num3 = int(n3)

print(int(num1+num2) % num3)
print(int(((num1%num3)+(num2%num3))%num3))
print(int((num1*num2)%num3))
print(((num1%num3) * (num2%num3))%num3)