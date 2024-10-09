"""
Make life easier with sparta
==================================

- build sparta: python main.py build -np 8
- prepare directory: python main.py prepare run/ examples/cylinder/
- run sparta: python main.py run run/ma2cylinder.cfg -np 32
- generate vtks: python main.py paraview run/
- clean vtks: python main.py rmgrid run/
- clean output: python main.py rmout run/
- clean build: python main.py unmake
"""

import easyspa as es

def main():
    args = es.parse_arguments()
    # adict = args.__dict__
    run = es.select_mode(args.mode)
    run(args)

if __name__ == "__main__":
    main()
