s = input("Enter string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels:", count)
