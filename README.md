# docs-scripts

I created these scripts to help manage the static site generator (Antora) and the content source files (in AsciiDoc) used to build [Kobiton Docs](https://docs.kobiton.com/).

## Scripts

| Name                 | Go to file                                 | Description                                                                                                                              |
|----------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `beautify_logs.py`   | [File](scripts/beautify_logs.py)           | Converts Antora's JSON logs into a "beautified," interactive table, so docs maintainers can open flagged files directly from their preview window.                |
| `cleanup_content.py` | [File](scripts/cleanup_content.py)         | Runs all scripts in the [modules directory](./modules) which: adds the module name to Antora attributes, fixes errors with spaces and periods, fixes newlines, and fixes URLs formatting.                   |
| `create_csv.py`      | [File](scripts/create_csv.py)              | Generates a CSV file with the following information for each document: title, section, subsection, and site URL.                                                   |
| `minify_css.py`      | [File](scripts/minify_css.py)              | Merges all human-readable CSS files from the [UI bundle directory](./ui-bundle/css) into a single, minifed file (`site.css`), which improves front-end development workflows while increasing site responsiveness. |

## Quick start

To run a script, you'll need to install [Python](https://www.python.org/downloads/). Run the following commands to see if it's installed:

```plaintext
python --version
```

If Python's installed, open the `scripts` directory.

```shell
cd <path-to-script-directory>/docs-scripts/scripts
```

Next, make each script executable in your shell environment.

```shell
chmod +x beautify_logs.py cleanup_content.py create_csv.py minify_css.py
```

Since there's a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) on the first line of every script (`#!/usr/bin/env python3`), you don't need to invoke Python manually. Simply enter the path to the script you'd like to use. For example:

```shell
./scripts/beautify_logs.py
```
