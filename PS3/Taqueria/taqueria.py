
def main():
    x = calc_total("Input: ")

    #to calculate the total of the items ordered.
def calc_total(prompt):
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0.00
    for i in menu:
        try:
            x = input(prompt).title()
            if x in menu:
                total = total + menu[x]
                print(f"Total: ${total:.2f}")
            elif x == "^D":
                break
            else:
                continue
        except KeyboardInterrupt as e:
            break
        except EOFError:
            break
        except KeyError as e:
            pass
        else:
            pass

main()
