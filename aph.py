#!/usr/bin/env python3

# Antora Project Helper

import subprocess
import argparse
from scripts.cleanup_content import main as general
from scripts.beautify_logs import main as beautify
from scripts.minify_css import main as minify
from scripts.create_csv import main as csv

PROJECT_ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()
parser = argparse.ArgumentParser(description="Manage your Antora project with APH.")

# Required argument(s)
parser.add_argument("directory",
                    nargs='?',
                    default=PROJECT_ROOT,
                    help="Your Antora project's root directory. By default, set to \'git rev-parse --show-toplevel\'.")

# Optional argument(s)
parser.add_argument("-g", "--general", help="Cleans up content.", action="store_true")
parser.add_argument("-b", "--beautify", help="Beautifies logs.", action="store_true")
parser.add_argument("-m", "--minify", help="Minifies CSS files.", action="store_true")
parser.add_argument("-c", "--csv", help="Creates CSV file.", action="store_true")


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    if args.general:
        general()
    elif args.beautify:
        beautify()
    elif args.minify:
        minify()
    elif args.csv:
        csv()
