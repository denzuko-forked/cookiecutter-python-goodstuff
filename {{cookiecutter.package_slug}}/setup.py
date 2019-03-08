"""Setup file for {{ cookiecutter.package_name }}"""


import subprocess
import setuptools


with open("README.md", "r") as fh:
    DESC = fh.read()


setuptools.setup(
    name="{{ cookiecutter.package_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.package_short_description }}",
    long_description=DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug}}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
