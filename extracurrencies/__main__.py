import sys
from pathlib import Path

from .currencies import compile_currencies
from .processing import process_files


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

    process_files(["source/base.json", f"source/base_{sys.argv[1]}.json"],
                  output="/universal/def/economy_data.sii",
                  stype="economy_data", sname="economy.data.storage",
                  extra=currencies)
    process_files(["source/manifest.json"],
                  output="/universal/manifest.sii",
                  stype="mod_package", sname=".universal")
    process_files(["source/versions.json"],
                  output="/versions.sii",
                  stype="package_version_info", sname=".universal")


if __name__ == "__main__":
    main()
