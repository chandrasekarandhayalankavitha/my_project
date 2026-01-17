
amt = int(input("Enter withdrawal amount: "))
if amt % 100 == 0:
    print(f"Dispensing {amt}")
else:
    print("Invalid amount")