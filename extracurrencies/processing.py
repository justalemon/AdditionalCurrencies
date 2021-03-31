import json
import sys

from colorama import Fore, Style

from .sii import from_dict


def process_files(game, sources, output, stype, sname, extra={}):
    """
    Processes the contents of the file(s).
    """
    files = ", ".join(x for x in sources if isinstance(x, str)) or "-"
    dicts = [x for x in sources if isinstance(x, dict)]
    print(f"Processing files {Fore.LIGHTGREEN_EX}{files}{Style.RESET_ALL} and {Fore.LIGHTGREEN_EX}{len(dicts)} "
          f"{Style.RESET_ALL}dictionaries to {Fore.LIGHTRED_EX}{output}{Style.RESET_ALL}")

    # Make a dict and load the source content
    content = {}
    for source in sources:
        if isinstance(source, str):
            with open(source) as file:
                content.update(json.load(file))
        elif isinstance(source, dict):
            content.update(source)
        else:
            name = content.__class__.__name__
            print(f"{Fore.RED}Error{Style.RESET_ALL}: Expected str or dict, found {name}")
            sys.exit(4)

    content.update(extra)
    # Now, save the SII content
    sii_str = from_dict(content, stype, sname)
    with open("build/" + game + output, "w", encoding="utf-8") as file:
        file.write(sii_str)
