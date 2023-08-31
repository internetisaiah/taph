from setuptools import setup, find_packages

setup(
    name='docs',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'beautify_logs=scripts.beautify_logs:main',
            'cleanup_content=scripts.cleanup_content:main',
            'create_csv=scripts.create_csv:main',
            'minify_css=scripts.minify_css:main',
        ],
    },
)
