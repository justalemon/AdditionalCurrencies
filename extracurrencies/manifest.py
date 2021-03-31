import os
import sys

from colorama import Fore, Style


def compile_manifest(appveyor: bool):
    """
    Compiles the Manifest to a SII Compatible dict.
    """
    if appveyor and "APPVEYOR_REPO_TAG_NAME" not in os.environ:
        print(f"{Fore.RED}Error{Style.RESET_ALL}: Environment Variable APPVEYOR_REPO_TAG_NAME is not present!")
        sys.exit(3)

    return {
        "display_name": "Additional Currencies for ETS2",
        "package_version": os.environ["APPVEYOR_REPO_TAG_NAME"] if appveyor else "2.0-pre",
        "author": "Lemon (justalemon)",
        "category@0": "other",
        "icon": "icon.jpg",
        "description_file": "description.txt"
    }
