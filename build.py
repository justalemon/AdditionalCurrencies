import json
import sys
from pathlib import Path

import sii


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


def process(sources, output, stype, sname, extra={}):
    """
    Processes the contents of the file(s).
    """
    # Make a dict and load the source content
    content = {}
    for source in sources:
        with open(source) as file:
            content.update(json.load(file))
    content.update(extra)
    # Now, save the SII content
    sii_str = sii.from_dict(content, stype, sname)
    with open("build/" + sys.argv[1] + output, "w", encoding="utf-8") as file:
        file.write(sii_str)


def main():
    print(f"Arguments: {sys.argv}")

    if len(sys.argv) > 2:
        print("Too Much arguments!")
        sys.exit(2)
    elif len(sys.argv) < 2:
        print("Too Many arguments!")
        sys.exit(3)

    Path("build/" + sys.argv[1] + "/universal/def").mkdir(parents=True, exist_ok=True)

    currencies = compile_currencies(sys.argv[1])

    process(["source/base.json", f"source/base_{sys.argv[1]}.json"],
            output="/universal/def/economy_data.sii",
            stype="economy_data", sname="economy.data.storage",
            extra=currencies)
    process(["source/manifest.json"],
            output="/universal/manifest.sii",
            stype="mod_package", sname=".universal")
    process(["source/versions.json"],
            output="/versions.sii",
            stype="package_version_info", sname=".universal")


if __name__ == "__main__":
    main()
