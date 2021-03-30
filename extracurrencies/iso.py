import xml.etree.ElementTree as ET
from datetime import datetime

from colorama import Fore, Style


def get_iso_currencies():
    """
    Gets the ISO 4217:2015 codes from the ISO page.
    """
    with open("iso4217.xml") as file:
        root = ET.fromstring(file.read())

    date = datetime.strptime(root.attrib["Pblshd"], "%Y-%m-%d")
    readable = date.strftime("%B %d, %Y")
    print(f"Using ISO database from {Fore.LIGHTYELLOW_EX}{readable}{Style.RESET_ALL}")

    found = []

    for currency in root.iter("Ccy"):
        text = currency.text

        if found.count(text) == 0:
            found.append(text)

    found.sort()
    return found
