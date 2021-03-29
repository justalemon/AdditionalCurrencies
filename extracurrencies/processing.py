import json
import sys

from colorama import Fore, Style

from .sii import from_dict


def process_files(sources, output, stype, sname, extra={}):
    """
    Processes the contents of the file(s).
    """
    print(f"Processing files {Fore.LIGHTGREEN_EX}{sources}{Style.RESET_ALL} "
          f"to {Fore.LIGHTRED_EX}{output}{Style.RESET_ALL}")

    # Make a dict and load the source content
    content = {}
    for source in sources:
        with open(source) as file:
            content.update(json.load(file))
    content.update(extra)
    # Now, save the SII content
    sii_str = from_dict(content, stype, sname)
    with open("build/" + sys.argv[1] + output, "w", encoding="utf-8") as file:
        file.write(sii_str)
