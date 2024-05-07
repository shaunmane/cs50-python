
wds = []

while True:
    try:
        item = input().upper()
        wds.append(item)
        if item == "^D":
            print(groc[i], i)
            break
        else:
            continue
    except EOFError:
        #print(wds)
        break
    except KeyboardInterrupt:
        for i in groc:
            print(groc[i], i)
print()

my_w = sorted(wds)
groc = dict()

for w in my_w:
    #print(w)
    if w in groc:
        groc[w] = groc[w] + 1
    else:
        groc[w] = 1

for i in groc:
    print(groc[i], i)
