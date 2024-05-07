import json
import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate"].replace(",", "")
        b = sys.argv[1]
        f_rate = float(rate) * float(b)
        print(f"${f_rate:,.4f}")

except requests.RequestException:
    sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number")