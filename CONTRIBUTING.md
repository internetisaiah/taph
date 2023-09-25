# [in-progress] `taph` contributing guidelines

Thanks for contributing to `taph`! Everyone here is expected to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) so be sure to review before contributing.

If you're new to open source or Antora, start with [First time contributors](#first-time-contributors), otherwise choose a topic below:

## Table of contents

- [Quick start](#quick-start)
- [First time contributors](#first-time-contributors)
- [Directory and file names](#directory-and-file-names)
- [Code and content style](#code-and-content-style)

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

## First time contributors

### Version control

Version control allows you to work on documents simultaneously without accidentally overwriting another contributor's work.

- [Learn about Git and GitHub](https://docs.github.com/en/get-started/using-git/about-git)
- [Get started with GitHub](https://docs.github.com/get-started/quickstart/hello-world)
- [Your first pull request](https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

### Static site generator

Antora is a static site generator that converts plain text files into HTML and creates a static site using the CSS files in the `ui-bundle` directory.

- [Learn about Antora](https://docs.antora.org/antora/latest/how-antora-works/)
- [Get started with Antora](https://docs.antora.org/antora/latest/install-and-run-quickstart/)

### File types and markup language

Antora documents are written in a plain-text markup language (AsciiDoc) and only contain written content--not design content--allowing teams to separate writing-related tasks from design-related tasks.

- [Learn about the AsciiDoc markup language](https://docs.asciidoctor.org/asciidoc/latest/)
- [Get started with the AsciiDoc markup language](https://asciidoctor.org/docs/asciidoc-writers-guide/)

## Directory and file names

All directories and files should adhere to the following:

| Naming Guideline                | Before               | After                   |
|---------------------------------|----------------------|-------------------------|
| Only lowercase letters          | `This Is My TITLE`   | `this is my title`      |
| Replace spaces with underscores | `this is my title`   | `this_is_my_title`      |
| Replace important symbols       | `i love c++ & c#`    | `i love cpp and csharp` |
| Remove unimportant symbols      | `this: is my title!` | `this is my title`      |

For example:

```plaintext
scripts
├── beautify_logs.py
├── csv.py
├── edit.py
└── minify_css.py
```

## Code and content style

To ensure consistency for `taph`'s code and content, use the following guidelines:

- [Google's Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
- [Google's Content Style Guide](https://developers.google.com/style/highlights)
