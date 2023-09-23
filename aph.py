#!/usr/bin/env python3

# Antora Project Helper

import subprocess
import argparse
from scripts.edit import main as general
from scripts.beautify import main as beautify
from scripts.minify import main as minify
from scripts.csv import main as csv

# Constants:
# Dictionary which maps optional arguments to corresponding functions in './scripts'.
APH_SCRIPTS = {
    'general': general,
    'beautify': beautify,
    'minify': minify,
    'csv': csv
}

# The Antora project's root directory.
PROJECT_ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()


# APH argument parser using Python's 'argparse'.
def main():
    parser = argparse.ArgumentParser(description="Manage your Antora project with APH.")

    # Argument(s)
    parser.add_argument("directory",
                        nargs='?',
                        default=PROJECT_ROOT,
                        help="your antora project's root directory "
                             "(default: the value of 'git rev-parse --show-toplevel')")
    parser.add_argument("-q", "--quiet",
                        help="suppresses all aph notifications",
                        action="store_true")
    parser.add_argument("-b", "--beautify",
                        help="beautify your logs by creating an asciidoc table containing cross-references "
                             "to each file which can be opened from your ide's preview window",
                        action="store_true")
    parser.add_argument("-m", "--minify",
                        help="copy all css content from your ui bundle directory into a single, minified file: 'site.css'",
                        action="store_true")
    parser.add_argument("-c", "--csv",
                        help="generate a '.csv' file containing the urls for the documents in your project's "
                             "output directory which can be imported later into a spreadsheet",
                        action="store_true")
    parser.add_argument("-e", "--edit",
                        help="make the following edits to each '.adoc' file in './docs/modules/': "
                             "fix newlines, fix urls, "
                             "add modules to asciidoc attributes,"
                             "add missing spaces after periods",
                        action="store_true")

    args = parser.parse_args()

    # Check the given optional argument(s) and run the matching function(s) from the 'aph_scripts' dictionary.
    for arg, script in APH_SCRIPTS.items():
        if getattr(args, arg):
            script()
            if not args.quiet:
                print(f"{arg} successfully executed.")

    # If no optional argument(s) given, notify user.
    if not any([getattr(args, key) for key in APH_SCRIPTS.keys()]):
        print("At least one optional argument is required for 'aph'. For more information, see '--help'.")


if __name__ == "__main__":
    main()
