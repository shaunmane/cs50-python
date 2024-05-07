
def main():
    x = input("What time is it? ").strip()
    time = convert(x)
    if time >= 18.00 and time <= 19.00:
        print("dinner time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 7.00 and time <= 8.00:
        print("breakfast time")

def convert(time):
    hours, minutes = time.split(":")
    z = float(hours) + float(minutes)/60
    return z

if __name__ == "__main__":
    main()


