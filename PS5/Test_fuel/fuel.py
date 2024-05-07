def main():
    fraction = input("Fraction: ")
    print(gauge(fraction))


def convert(fraction):
    try:
        d, n = fraction.split("/")
        percentage = round((int(d) / int(n)) * 100)
        return percentage
    except AttributeError:
        return fraction
    except ValueError:
        return main()
    except ZeroDivisionError:
        return main()
    else:
        pass


def gauge(percentage):
    try:
        if convert(percentage) >= 95 and convert(percentage) <= 100:
            return "F"
        elif convert(percentage) >= 0 and convert(percentage) <= 5:
            return "E"
        elif (
            convert(percentage) == 75
            or convert(percentage) == 25
            or convert(percentage) == 50
            or convert(percentage) == 33
            or convert(percentage) == 67
            ):
            return f"{convert(percentage)}%"
        elif convert(percentage) > 100:
            return main()
        else:
            return main()
    except TypeError:
        pass
    else:
        pass


if __name__ == "__main__":
    main()

