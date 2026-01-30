cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No profit no loss")
