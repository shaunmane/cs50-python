
due = 50
while due != 0:
    coin = int(input("Insert Coin: "))
    change_owed = coin - due
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
        if  due <= 0:
            print(f"Change Owed: {change_owed}")
            break
        print(f"Amount Due: {due}")
    elif due <= 0:
        print(f"Change owed: {change_owed}")
    else:
        print(f"Amount Due: {due}")
