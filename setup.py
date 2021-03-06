from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from differently.version import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Software Development :: Testing",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="CLI tool and package for visualising the differences between things",
    entry_points={
        "console_scripts": [
            "differently=differently.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "ansiscape>=1.1.0",
        "pyyaml",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="differently",
    packages=[
        "differently",
        "differently.version",
    ],
    package_data={
        "differently": ["py.typed"],
        "differently.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/differently",
    version=version,
)
