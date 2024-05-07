
while True:
    try:
        x = input("Fraction: ")
        d, n = x.split("/")
        b = int(round((int(d)/int(n))*100))
        if b >= 95 and b <= 100:
            print("F")
        elif b >= 0 and b <= 5:
            print("E")
        elif b == 75 or b == 25 or b == 50 or b == 33 or b == 67:
            print(f"{b}%")
        elif b > 100:
            continue
        else:
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
