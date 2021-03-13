import json
import sys
from pathlib import Path

import sii


def main():
    print(f"Arguments: {sys.argv}")

    if len(sys.argv) > 2:
        print("Too Much arguments!")
        sys.exit(2)
    elif len(sys.argv) < 2:
        print("Too Many arguments!")
        sys.exit(3)

    Path("build/" + sys.argv[1] + "/universal/def").mkdir(parents=True, exist_ok=True)

    with open("source/base.json") as file:
        economy_base = json.load(file)
    with open(f"source/base_{sys.argv[1]}.json") as file:
        extra = json.load(file)
    economy_base.update(extra)
    economy = sii.from_dict(economy_base, "economy_data", "economy.data.storage")
    with open("build/" + sys.argv[1] + "/universal/def/economy_data.sii", "w") as file:
        file.write(economy)

    with open("source/manifest.json") as file:
        manifest_base = json.load(file)
    manifest = sii.from_dict(manifest_base, "mod_package", ".universal")
    with open("build/" + sys.argv[1] + "/universal/manifest.sii", "w") as file:
        file.write(manifest)

    with open("source/versions.json") as file:
        versions_base = json.load(file)
    versions = sii.from_dict(versions_base, "package_version_info", ".universal")
    with open("build/" + sys.argv[1] + "/versions.sii", "w") as file:
        file.write(versions)


if __name__ == "__main__":
    main()
