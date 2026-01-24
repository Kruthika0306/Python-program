n = int(input("How many elements: "))
lst = []
s = 0

for i in range(n):
    x = int(input("Enter number: "))
    lst.append(x)
    s += x

print("Sum:", s)
