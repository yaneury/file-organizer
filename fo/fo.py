#!/usr/bin/env python3

import argparse

from categorize import CategorizeCommand
from dedupe import DedupeCommand
from split import SplitCommand
    

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        help="Select command to run", required=True, dest="cmd")

    cmds = [CategorizeCommand(), DedupeCommand(), SplitCommand()]

    for c in cmds:
        c.prepare(subparsers.add_parser(c.NAME, help=c.HELP))

    args = parser.parse_args()

    for c in cmds:
        if args.cmd == c.NAME:
            c.execute(args)
            parser.exit(0)

    parser.exit(1)


if __name__ == "__main__":
    main()
