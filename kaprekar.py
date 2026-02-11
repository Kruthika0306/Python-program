def is_kaprekar(num):
    square = str(num ** 2)

    for i in range(1, len(square)):
        left = int(square[:i])
        right = int(square[i:])

        if right != 0 and left + right == num:
            return True

    return False


def main():
    number = int(input("Enter a number: "))

    if is_kaprekar(number):
        print(f"{number} is a Kaprekar number.")
    else:
        print(f"{number} is NOT a Kaprekar number.")


if __name__ == "__main__":
    main()
