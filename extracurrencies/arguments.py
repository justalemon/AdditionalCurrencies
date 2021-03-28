import argparse


def parse_arguments():
    """
    Parses the command line arguments.
    """
    parser = argparse.ArgumentParser(description="Compiles the ExtraCurrencies mod")
    parser.add_argument("game", choices=["ets2", "ats"],
                        help="the game to target")

    return parser.parse_args()


args = parse_arguments()
