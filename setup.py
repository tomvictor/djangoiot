#!/usr/bin/env python
from setuptools import (
    setup,
    find_packages,
)
import re

with open('iotcore/__version__.py', 'rb') as f:
    VERSION = str(eval(re.search(r'version\s+=\s+(.*)',
                                 f.read().decode('utf-8')).group(1)))

BINARY = "goiotbackend"

GO_BINARY = [
    f"{BINARY}-mac-{VERSION}",
    f"{BINARY}-win-{VERSION}.exe",
    f"{BINARY}-linux-{VERSION}",
]

extras_require = {
    "test": [
        "cryptography",
        "pytest-cov",
        "pytest-django",
        "pytest-xdist",
        "pytest",
        "tox",
    ],
    "lint": ["flake8", "pep8", "isort", ],
    "doc": ["Sphinx>=1.6.5,<2", "sphinx_rtd_theme>=0.1.9", ],
    "dev": ["bumpversion>=0.5.3,<1", "pytest-watch", "wheel", "twine", "ipython", ],
}

extras_require["dev"] = (
        extras_require["dev"]
        + extras_require["test"]  # noqa: W504
        + extras_require["lint"]  # noqa: W504
        + extras_require["doc"]  # noqa: W504  # noqa: W504
)

master_doc = "index"
setup(
    name="iotcore",
    version=VERSION,
    url="https://github.com/tomvictor/iotcore",
    license="MIT",
    description="Enable IoT in you django app",
    # long_description=open("README.rst", "r", encoding="utf-8").read(),
    long_description="add iotcore to your django apps. check docs at https://github.com/tomvictor/iotcore for more "
                     "details",
    author="Tom Victor",
    author_email="vjtomvictor@gmail.com",
    install_requires=[
        "psutil",
    ],
    python_requires=">=3.6",
    extras_require=extras_require,
    packages=find_packages(
        exclude=["tests", "docs", "tests.*", "licenses", "requirements"]
    ),
    include_package_data=True,
    package_data={"": GO_BINARY},
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
