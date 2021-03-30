import json
import sys

from colorama import Fore, Style


def compile_currencies(game):
    """
    Compiles the currencies into a SII compatible dictionary.
    """
    with open("currencies.json", encoding="utf-8") as file:
        currencies = json.load(file)

    currencies.sort(key=lambda x: x["name"])

    new = {}
    i = 1

    for currency in currencies:
        print(f"Adding currency {Fore.GREEN}" + currency["name"] + f"{Style.RESET_ALL} with ISO 4217 code "
              f"{Fore.LIGHTMAGENTA_EX}" + str(currency["iso"]) + f"{Style.RESET_ALL}")

        number = str(i).rjust(3, "0")
        new["currency_code@" + number] = "{0} ({1})".format(currency["name"], currency["iso"])
        new["currency_ratio@" + number] = currency["rate"][game]
        new["currency_sign1@" + number] = currency["sign"][0]
        new["currency_sign2@" + number] = currency["sign"][1]
        new["currency_sign3@" + number] = currency["sign"][2]
        i += 1

    return new
