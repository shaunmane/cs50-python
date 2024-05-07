
months = {
    "January" : "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }

while True:
    try:
        x = input("Date: ")
        if x[0].isalpha() and "/" in x:
            break
        elif x[0].isalpha() and "," not in x:
            break
        elif "/" in x:
            n = x.strip()
            m, d, y = n.split("/")
            if int(m) >= 13:
                continue
            elif int(d) >= 32:
                continue
            else:
                print(f"{y}-{m:0>2}-{d:0>2}")
            break
        elif x[0].isalpha():
            b = x.rsplit()
            c = b[0]
            d = b[1].replace(",","")
            if int(d) >= 32:
                continue
            else:
                print(f"{b[-1]}-{months[c]:0>2}-{d:0>2}")
            break
        else:
            continue
    except EOFError:
        break
    except KeyboardInterrupt:
        break

