import json
import sys

from colorama import Fore, Style

INVALID = {
    "BOV": "For use in Country only, No EUR/USD Conversion",
    "CHE": "Complementary Currency",
    "CHW": "Complementary Currency",
    "COU": "For use in Country only, No EUR/USD Conversion",
    "CUC": "Demonetization in progress",
    "USN": "Same as USD, No EUR Conversion",
    "UYI": "For use in Country only, No EUR/USD Conversion",
    "UYW": "For use in Country only, No EUR/USD Conversion",
    "XAG": "Silver, one troy ounce",
    "XAU": "Gold, one troy ounce",
    "XBA": "Unused European Bond Market Unit: EURCO",
    "XBB": "Unused European Bond Market Unit: E.M.U.-6",
    "XBC": "Unused European Bond Market Unit: E.U.A.-9",
    "XBD": "Unused European Bond Market Unit: E.U.A.-17",
    "XDR": "Special Drawing Rights, International Monetary Fund",
    "XPD": "Palladium, one troy ounce",
    "XPT": "Platinum, one troy ounce",
    "XSU": "SUCRE, not a convertible currency per design",
    "XTS": "Code used for testing",
    "XUA": "Internal use by African Development Bank",
    "XXX": "No Currency",
    "ZWL": "Obsolete"
}


def load_currencies():
    """
    Loads the currencies from currencies.json
    """
    with open("currencies.json", encoding="utf-8") as file:
        currencies = json.load(file)
    currencies.sort(key=lambda x: x["name"])
    return currencies


def compile_currencies(game, currencies, iso):
    """
    Compiles the currencies into a SII compatible dictionary.
    """
    new = {}
    done = []
    i = 1

    for currency in currencies:
        if done.count(currency["iso"]) != 0:
            print(f"{Fore.YELLOW}Warning{Style.RESET_ALL}: Currency with ISO Code {Fore.LIGHTMAGENTA_EX}"
                  f"{currency['iso']}{Style.RESET_ALL} is duplicated!")
            continue
        elif currency["iso"] not in iso:
            print(f"{Fore.YELLOW}Warning{Style.RESET_ALL}: ISO Code {Fore.LIGHTMAGENTA_EX}{currency['iso']}"
                  f"{Style.RESET_ALL} is not valid!")
            continue

        print(f"Adding currency {Fore.GREEN}" + currency["name"] + f"{Style.RESET_ALL} with ISO 4217 code "
              f"{Fore.LIGHTMAGENTA_EX}" + str(currency["iso"]) + f"{Style.RESET_ALL}")

        number = str(i).rjust(3, "0")
        new["currency_code@" + number] = "{0} ({1})".format(currency["name"], currency["iso"])
        new["currency_ratio@" + number] = currency["rate"][game]
        new["currency_sign1@" + number] = currency["sign"][0]
        new["currency_sign2@" + number] = currency["sign"][1]
        new["currency_sign3@" + number] = currency["sign"][2]
        i += 1

        done.append(currency["iso"])

    for code in (x for x in iso if x not in done):
        if code in INVALID:
            print(f"{Fore.BLUE}Info{Style.RESET_ALL}: Currency with ISO Code {Fore.LIGHTMAGENTA_EX}"
                  f"{code}{Style.RESET_ALL} was marked as invalid: {INVALID[code]}")
        else:
            print(f"{Fore.RED}Error{Style.RESET_ALL}: Currency information for ISO Code {Fore.LIGHTMAGENTA_EX}"
                  f"{code}{Style.RESET_ALL} was not found!")
            sys.exit(2)

    return new
