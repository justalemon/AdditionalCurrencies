from pathlib import Path

from colorama import init, Fore, Style

from .arguments import args
from .currencies import load_currencies, compile_currencies
from .iso import get_iso_currencies
from .processing import process_files


def main():
    if hasattr(args, "help"):
        return

    init()
    print("Starting ExtraCurrencies Build System")

    iso = get_iso_currencies()
    currencies = load_currencies()

    for game in args.games:
        print(f"Processing Game {Fore.LIGHTBLUE_EX}{game.upper()}{Style.RESET_ALL}")

        Path("build/" + game + "/universal/def").mkdir(parents=True, exist_ok=True)

        print(f"Compiling list of Currencies for game {Fore.LIGHTBLUE_EX}{game.upper()}{Style.RESET_ALL}")
        game_currencies = compile_currencies(game, currencies, iso)

        process_files(["source/base.json", f"source/base_{game}.json"],
                      output="/universal/def/economy_data.sii",
                      stype="economy_data", sname="economy.data.storage",
                      extra=game_currencies)
        process_files(["source/manifest.json"],
                      output="/universal/manifest.sii",
                      stype="mod_package", sname=".universal")
        process_files(["source/versions.json"],
                      output="/versions.sii",
                      stype="package_version_info", sname=".universal")

        print(f"Completed processing for game {Fore.LIGHTBLUE_EX}{game.upper()}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
