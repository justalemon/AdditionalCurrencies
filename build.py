import json
import sys

import sii


def main():
    print(f"Arguments: {sys.argv}")

    if len(sys.argv) > 2:
        print("Too Much arguments!")
        sys.exit(2)
    elif len(sys.argv) < 2:
        print("Too Many arguments!")
        sys.exit(3)

    with open("source/base.json") as file:
        base = json.load(file)
    with open(f"source/base_{sys.argv[1]}.json") as file:
        extra = json.load(file)

    base.update(extra)

    string = sii.from_dict(base, "economy_data", "economy.data.storage")
    with open("test.sii", "w") as file:
        file.write(string)


if __name__ == "__main__":
    main()
