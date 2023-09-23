# taph

`taph`, The Antora Project Helper, is a Python-based, command-line tool allowing you to easily beautify logs, minify CSS files, and more.

These scripts were originally created to help manage my _own_ Antora project, so their usefulness to your own project may vary. Before you understand each script before using them.

You can run one or more script at a time by passing optional arguments to `./taph.py`. For more information, see [Arguments](#arguments).

## Quick start

To run a script, you'll need to install [Python](https://www.python.org/downloads/). Run the following commands to see if it's installed:

```plaintext
python --version
```

If Python's installed, make `./taph.py` executable in your shell environment.

```shell
chmod +x <path-to-taph>/taph.py
```

Pass one or more scripts as optional arguments to `.taph.py`. For example:

```shell
./taph.py -b -m
```

To see the full list of arguments, use `--help`.

```shell
./taph.py --help
```

## Arguments

### Positional argument

Only one positional argument is required: `directory`. If `directory` isn't set, the value of `git rev-parse --show-toplevel` will be used instead.

| Argument    | Default value                   | Description                           |
|-------------|---------------------------------|---------------------------------------|
| `directory` | `git rev-parse --show-toplevel` | Your antora project's root directory. |

### Optional arguments

At least one optional argument is required, however more than one optional argument can be used at once, such as `./taph.py -b -m`.

| Argument   | Accepted value(s)  | Go to file                                     | Description                                                                                                                                                       |
|------------|--------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `help`     | `-h`, `--help`     | N/A                                            | Show this help message and exit.                                                                                                                                  |
| `quiet`    | `-q`, `--quiet`    | N/A                                            | Suppress all `taph` notifications in the terminal.                                                                                                                |
| `beautify` | `-b`, `--beautify` | [`./scripts/beautify.py`](scripts/beautify.py) | Beautify your logs by creating an asciidoc table containing cross-references to each file which can be opened from your ide's preview window.                     |
| `minify`   | `-m`, `--minify`   | [`./scripts/minify.py`](scripts/minify.py)     | Copy all css content from your ui bundle directory into a single, minified file: `site.css`.                                                                      |
| `csv`      | `-c`, `--csv`      | [`./scripts/csv.py`](scripts/csv.py)           | Generate a `.csv` file containing the urls for the documents in your project's output directory which can be imported later into a spreadsheet.                   |
| `edit`     | `-e`, `--edit`     | [`./scripts/edit.py`](scripts/edit.py)         | Make the following edits to each `.adoc` file in `./docs/modules/`: fix newlines, fix urls, add modules to asciidoc attributes, add missing spaces after periods. |
