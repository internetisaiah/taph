# docs-scripts

These are scripts I created to docs maintainers manage the static site generator (Antora) and content source files (in AsciiDoc) used to build [Kobiton Docs](https://docs.kobiton.com/).

## Scripts

* `beautify_logs.py`: [this script](scripts/beautify_logs.py) converts Antora's JSON logs into an interactive table, allowing docs maintainers to directly open files from their text editor's preview window.
* `cleanup_content.py`: [this script](scripts/cleanup_content.py) runs the scripts in the [modules directory](./modules) which collectively: adds the Antora module to all 'xref' and 'image' attributes, adds missing spaces after periods, fixes all newlines in each file, and fixes all URLs.
* `create_csv.py`: [this script](scripts/create_csv.py) generates a Comma-Separated Values (CSV) file where each doc is added to a row along with its title, section, subsection(s), and URL.
* `minify_css.py`: [this script](scripts/minify_css.py) navigates to the CSS directory within the UI bundle of a standard Antora configuration (`<project-root>/ui-bundle/css/`), then merges all beautified CSS files together into a single file (`site.css`), so front-end maintainers can easily work on design elements while still maximizing site responsiveness.

## Quick start

To run a script, you'll need [Python](https://www.python.org/downloads/). Run the following commands to check if they're installed:

```plaintext
python --version
```

If Python's installed, open the script directory.

```shell
cd <path-to-script-directory>
```

Make each script executable in your shell environment.

```shell
chmod +x beautify_logs.py cleanup_content.py create_csv.py minify_css.py
```

Since a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) is located on the first line of each script (`#!/usr/bin/env python3`), you don't need to invoke Python to use these scripts. Simply call the path to the script you'd like to use.

```shell
<path-to-script-directory>/beautify_logs.py
```
