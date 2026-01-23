n = int(input("How many elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter number: ")))

key = int(input("Enter key: "))
found = False

for x in lst:
    if x == key:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
