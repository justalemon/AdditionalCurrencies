import json
import sys
from pathlib import Path

import sii


def process(*sources, output, stype, sname):
    """
    Processes the contents of the file(s).
    """
    # Make a dict and load the source content
    content = {}
    for source in sources:
        with open(source) as file:
            content.update(json.load(file))
    # Now, save the SII content
    sii_str = sii.from_dict(content, stype, sname)
    with open("build/" + sys.argv[1] + output, "w") as file:
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

    process("source/base.json", f"source/base_{sys.argv[1]}.json",
            output="/universal/def/economy_data.sii",
            stype="economy_data", sname="economy.data.storage")
    process("source/manifest.json",
            output="/universal/manifest.sii",
            stype="mod_package", sname=".universal")
    process("source/versions.json",
            output="/versions.sii",
            stype="package_version_info", sname=".universal")


if __name__ == "__main__":
    main()
