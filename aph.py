#!/usr/bin/env python3

# Antora Project Helper

import subprocess
import argparse
from scripts.general import main as general
from scripts.beautify import main as beautify
from scripts.minify import main as minify
from scripts.csv import main as csv

PROJECT_ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()
parser = argparse.ArgumentParser(description="Manage your Antora project with APH.")

# Argument(s)
parser.add_argument("directory",
                    nargs='?',
                    default=PROJECT_ROOT,
                    help="the antora project's root directory (default: the value of '%(default)s')")
parser.add_argument("-g", "--general",
                    help="a general cleanup script to add the relative module to each asciidoc attribute,"
                         "add missing spaces after periods, fix newlines, and fix url strings",
                    action="store_true")
parser.add_argument("-b", "--beautify",
                    help="beautifies the logs in 'logs/' by creating an asciidoc table with cross-references "
                         "to each file that can be opened directly from the preview window",
                    action="store_true")
parser.add_argument("-m", "--minify",
                    help="copies all css content from the ui bundle directory into a single, minified file: 'site.css'",
                    action="store_true")
parser.add_argument("-c", "--csv",
                    help="creates a '.csv' file with all site urls which can"
                         " be imported to one or more spreadsheets for docs reviews",
                    action="store_true")
# TODO: make 'quiet' command


if __name__ == "__main__":
    args = parser.parse_args()

    if args.general:
        general()
    elif args.beautify:
        beautify()
    elif args.minify:
        minify()
    elif args.csv:
        csv()
