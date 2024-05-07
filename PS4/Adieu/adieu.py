import inflect

p = inflect.engine()

alist = []
while True:
    try:
        name = input("Name: ")
        alist.append(name)
        mylist = p.join((alist))
    except EOFError:
        print(f"\nAdieu, adieu, to {mylist}")
        break
