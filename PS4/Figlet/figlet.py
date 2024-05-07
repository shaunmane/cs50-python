import sys
from pyfiglet import Figlet

try:
    if len(sys.argv) == 1:
        f = Figlet(font='standard')
        x = input("Input: ")
        print(f.renderText(x))
    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        f = Figlet(font=sys.argv[2])
        figlet = Figlet()
        list = figlet.getFonts()
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list:
            x = input("Input: ")
            print(f.renderText(x))
        elif sys.argv[2] not in list:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid usage")
except:
    sys.exit("Invalid Usage")