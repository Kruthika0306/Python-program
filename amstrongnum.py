n = int(input("Enter number: "))
temp = n
s = 0

while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10

if temp == s:
    print("Armstrong")
else:
    print("Not Armstrong")
