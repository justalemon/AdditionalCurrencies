import argparse


def parse_arguments():
    """
    Parses the command line arguments.
    """
    parser = argparse.ArgumentParser(description="Compiles the ExtraCurrencies mod")
    parser.add_argument("games", choices=["ets2", "ats"], nargs="+",
                        help="the game(s) to target")

    return parser.parse_args()


args = parse_arguments()
