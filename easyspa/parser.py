import argparse

def parse_arguments():
    """
    Parse command-line arguments

    Returns:
        Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="easyspa", description="To make life easier with sparta."
    )

    parser.add_argument("mode", nargs="+", help="execution mode")

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        # required=True,
        help="Path to the input file.",
    )
    parser.add_argument("-np", default=1, type=int, help="number of processors")
    parser.add_argument("-x", default=100, type=int, help="number of post-processing batch grids in x-axis")

    args = parser.parse_args()
    return args
