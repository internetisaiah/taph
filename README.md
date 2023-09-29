# `taph`

`taph`, The Antora Project Helper, is a Python-based, command-line tool which enables you to easily beautify logs, minify CSS files, create CSV files, and more. These scripts were originally created to help manage my _own_ Antora projects, so their usefulness to you may vary. For more information about each script, see [Arguments](#arguments).

If you'd like to help improve `taph`, you can:

- [Report an issue](https://github.com/internetisaiah/taph/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)
- [Request a feature](https://github.com/internetisaiah/taph/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)
- [Contribute](CONTRIBUTING.md)

## Quick start

First, check if [Python](https://www.python.org/downloads/) is installed.

```plaintext
python --version
```

If Python's installed, make `./taph.py` executable in your shell environment.

```shell
chmod +x <path-to-taph>/taph.py
```

You can pass one or more optional arguments to `./taph.py`. For example:


```shell
$ ./taph.py -b -m
```

The output is the following:

```shell
'beautify' ran successfully.
'minify' ran successfully.
```

To see all available arguments, use `--help`.

```shell
./taph.py --help
```

## Arguments

### Positional argument

Only one positional argument is always required: `directory`. If `directory` is unassigned, the value of `git rev-parse --show-toplevel` will be used instead.

| Argument    | Default value                   | Description                           |
|-------------|---------------------------------|---------------------------------------|
| `directory` | `git rev-parse --show-toplevel` | Your antora project's root directory. |

### Optional arguments

_At least one_ optional argument is required, however you can use more than one at a time to run multiple scripts. For example:

```shell
$ ./taph.py -b -m

'beautify' ran successfully.
'minify' ran successfully.
```

| Argument   | Accepted value(s)  | Go to file                                     | Description                                                                                                                                                       |
|------------|--------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `help`     | `-h`, `--help`     | N/A                                            | Show this help message and exit.                                                                                                                                  |
| `quiet`    | `-q`, `--quiet`    | N/A                                            | Suppress all `taph` notifications in the terminal.                                                                                                                |
| `beautify` | `-b`, `--beautify` | [`./scripts/beautify.py`](scripts/beautify.py) | Beautify your logs by creating an asciidoc table containing cross-references to each file which can be opened from your text editor's preview window.                     |
| `minify`   | `-m`, `--minify`   | [`./scripts/minify.py`](scripts/minify.py)     | Copy all css content from your ui bundle directory into a single, minified file: `site.css`.                                                                      |
| `csv`      | `-c`, `--csv`      | [`./scripts/csv.py`](scripts/csv.py)           | Generate a `.csv` file containing the urls for the documents in your project's output directory which can be imported later into a spreadsheet.                   |
| `edit`     | `-e`, `--edit`     | [`./scripts/edit.py`](scripts/edit.py)         | Make the following edits to each `.adoc` file in `./docs/modules/`: fix newlines, fix urls, add modules to asciidoc attributes, add missing spaces after periods. |
