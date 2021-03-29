import re

from colorama import Fore, Style

from .arguments import args

pattern = re.compile("([A-Za-z_0-90-9]*)(@)?(tuple)?([0-9]*)?")


def vprint(text):
    if args.verbose:
        print(text)


def from_dict(contents: dict, stype: str, sname: str):
    """
    Dumps a SII-styled dictionary into an actually SII file.
    """
    string = "SiiNunit\n{\n    " + stype + " : " + sname + "\n    {\n"

    for key, value in contents.items():
        match = pattern.match(key)
        groups = match.groups()
        name = groups[0]

        # Convert the item to the correct format
        if isinstance(value, str):
            val = f"\"{value}\""
        elif "@" in groups and "tuple" in groups:
            val = str(tuple(value))
        else:
            val = str(value)

        if "@" in groups and groups[3].isnumeric():
            vprint(f"Writing to SII: {Fore.LIGHTCYAN_EX}{name}[]: {val}{Style.RESET_ALL}")
            string += "        " + groups[0] + "[]: " + val + "\n"
        elif isinstance(value, list) and "tuple" not in groups:
            i = 0
            for item in value:
                if isinstance(item, list):
                    item = tuple(item)
                vprint(f"Writing to SII: {Fore.LIGHTCYAN_EX}{name}[{i}]: {item}{Style.RESET_ALL}")
                string += "        " + groups[0] + f"[{i}]: " + str(item) + "\n"
                i += 1
        else:
            vprint(f"Writing to SII: {Fore.LIGHTCYAN_EX}{name}: {val}{Style.RESET_ALL}")
            string += "        " + groups[0] + ": " + val + "\n"

    string += "    }\n}\n"

    return string
