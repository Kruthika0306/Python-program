def calculate_bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return (100 * 1.5) + (units - 100) * 2.5
    else:
        return (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

def main():
    print("ELECTRICITY BILL CALCULATOR")

    units = int(input("Enter units consumed: "))
    bill = calculate_bill(units)

    print("Total Units:", units)
    print("Total Bill: ₹", bill)

    if units > 250:
        print("Tip: Reduce usage during peak hours")

if __name__ == "__main__":
    main()