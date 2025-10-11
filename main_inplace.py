# %%
import easyspa as es
import argparse
import os
# %%
def main_dirc():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
# %%
parser = argparse.ArgumentParser(
        prog="easyspa", description="To make life easier with sparta."
    )
parser.add_argument("mode", nargs="+", help="execution mode")
parser.add_argument(
    "-i",
    "--input",
    type=str,
    help="Path to the input file.",
)
parser.add_argument("-np", default=1, type=int, help="number of processors")
# %%
args = parser.parse_args(['build', '-np', '8'])
es.build_sparta(args)
# %%
main_dirc()
# regenerate Namespace
args = parser.parse_args(['prepare', 'run/', 'examples/config/cylinder/'])
es.prepare_simulation(args)
# %%
args = parser.parse_args(['run', 'run/ma2cylinder.cfg', '-np', '32'])
es.run_simulation(args)
# %%
