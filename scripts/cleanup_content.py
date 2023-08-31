#!/usr/bin/env python3

# Cleans up the content in '<project-root>/docs/utils/' using the scripts in the 'utils' directory:
# 'add_module_to_attributes': Adds the module to all 'xref' and 'image' AsciiDoc attributes
# 'add_spaces_after_periods': Adds missing spaces after periods
# 'fix_newlines': Fixes all newlines
# 'fix_urls': Fixes all URLs

import os
import glob
import importlib
from utils.get_project_root import get_project_root

# Scripts to run from './utils'.
SCRIPTS = {
    'add_module_to_attributes': 'utils.add_module_to_attributes.add_module_to_attributes',
    'add_spaces_after_periods': 'utils.add_spaces_after_periods.add_spaces_after_periods',
    'fix_newlines': 'utils.fix_newlines.fix_newlines',
    'fix_urls': 'utils.fix_urls.fix_urls'
}

# Directories in '<project-root>/docs/utils/' to ignore.
IGNORED_DIRECTORIES = ['release-notes', 'widget', 'about-version', 'ROOT']


# Go to '<project-root>/docs/utils/' and run all 'SCRIPTS' against each file not in 'IGNORED_DIRECTORIES'.
def main():
    root = get_project_root()
    modules_path = os.path.join(root, 'docs', '../utils')

    for module in os.listdir(modules_path):
        module_path = os.path.join(modules_path, module)
        if not os.path.isdir(module_path) or module in IGNORED_DIRECTORIES:
            continue

        for filename in glob.glob(module_path + '/**/*.adoc', recursive=True):
            if not any(ignore_dir in os.path.relpath(filename, module_path).split(os.sep)
                       for ignore_dir in IGNORED_DIRECTORIES):

                # Dynamically load and execute scripts
                for func_name in SCRIPTS.values():
                    module_name, function_name = '.'.join(func_name.split('.')[:-1]), func_name.split('.')[-1]
                    module = importlib.import_module(module_name)
                    getattr(module, function_name)(filename)


if __name__ == "__main__":
    main()
