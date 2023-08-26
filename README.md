# docs-scripts

I created these scripts to manage the static site generator (Antora) and source files (in AsciiDoc) used to build [Kobiton Docs](https://docs.kobiton.com/).

## Scripts

| Name                 | URL                                       | Description                                                                                                                              |
|----------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `beautify_logs.py`   | [URL](scripts/beautify_logs.py)           | Converts Antora's JSON logs into an interactive table, allowing docs maintainers to open files from their preview window.                |
| `cleanup_content.py` | [URL](scripts/cleanup_content.py)         | Runs scripts in the [modules directory](./modules) which add Antora module attributes, fix spaces, newlines, and URLs.                   |
| `create_csv.py`      | [URL](scripts/create_csv.py)              | Generates a CSV file with doc information like title, sections, subsections, and URLs.                                                   |
| `minify_css.py`      | [URL](scripts/minify_css.py)              | Merges beautified CSS files into a single file (`site.css`) for front-end maintainers to work on design while maximizing responsiveness. |


## Quick start

To run a script, you'll need to install [Python](https://www.python.org/downloads/). Run the following commands to see if it's installed:

```plaintext
python --version
```

If Python's installed, open the `scripts` directory.

```shell
cd <path-to-script-directory>/docs-scripts/scripts
```

Make each script executable in your shell environment.

```shell
chmod +x beautify_logs.py cleanup_content.py create_csv.py minify_css.py
```

Since a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) is located on the first line of each script (`#!/usr/bin/env python3`), you don't need to invoke Python to use these scripts. Simply enter the path to the script you'd like to use. For example:

```shell
./scripts/beautify_logs.py
```
