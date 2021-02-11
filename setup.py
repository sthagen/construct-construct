#!/usr/bin/env python
from setuptools import setup
from construct.version import version_string

setup(
    name = "construct",
    version = version_string,
    packages = [
        'construct',
        'construct.lib',
    ],
    license = "MIT",
    description = "A powerful declarative symmetric parser/builder for binary data",
    long_description = open("README.rst").read(),
    platforms = ["POSIX", "Windows"],
    url = "http://construct.readthedocs.org",
    author = "Arkadiusz Bulski, Tomer Filiba, Corbin Simpson",
    author_email = "arek.bulski@gmail.com, tomerfiliba@gmail.com, MostAwesomeDude@gmail.com",
    python_requires = ">=3.6",
    install_requires = [],
    extras_require = {
        "extras": [
            "enum34",
            "numpy",
            "arrow",
            "ruamel.yaml",
            "cloudpickle",
            "lz4",
        ],
    },
    keywords = [
        "construct",
        "kaitai",
        "declarative",
        "data structure",
        "struct",
        "binary",
        "symmetric",
        "parser",
        "builder",
        "parsing",
        "building",
        "pack",
        "unpack",
        "packer",
        "unpacker",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
