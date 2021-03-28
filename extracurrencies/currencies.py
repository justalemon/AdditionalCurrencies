import json
import sys


def compile_currencies(game):
    """
    Compiles the currencies into a SII compatible dictionary.
    """
    with open("currencies.json", encoding="utf-8") as file:
        currencies = json.load(file)

    max_c = 0

    for currency in currencies:
        num = currency["order"][game]
        if num > max_c:
            max_c = num

    if max_c + 1 < len(currencies):
        print(f"Count and Order don't match!")
        print(f"Expected {len(currencies)}, got ({max_c + 1})")
        sys.exit(4)

    currencies.sort(key=lambda x: x["order"][game])

    new = {}
    slots = []
    i = 1

    for currency in currencies:
        print("Adding currency " + currency["name"] + " on slot " + str(currency["order"][game]))

        if currency["order"][game] in slots:
            print("Currency with ID of " + currency["order"][game] + " is already present!")
            sys.exit(5)
        slots.append(currency["order"][game])

        number = str(i).rjust(3, "0")
        new["currency_code@" + number] = currency["name"]
        new["currency_ratio@" + number] = currency["rate"][game]
        new["currency_sign1@" + number] = currency["sign"][0]
        new["currency_sign2@" + number] = currency["sign"][1]
        new["currency_sign3@" + number] = currency["sign"][2]
        i += 1

    return new
