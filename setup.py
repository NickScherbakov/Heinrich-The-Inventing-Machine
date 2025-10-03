"""
Setup configuration for Heinrich TRIZ Engine
"""

from setuptools import setup, find_packages
from heinrich.version import __version__, __author__, __description__

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="heinrich-triz",
    version=__version__,
    author=__author__,
    author_email="contact@heinrich-triz.org",
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyYAML>=6.0",
        "numpy>=1.21.0",
        "dataclasses-json>=0.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "api": [
            "fastapi>=0.100.0",
            "uvicorn>=0.20.0",
        ],
        "ui": [
            "rich>=12.0.0",
            "colorama>=0.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "heinrich=heinrich_cli:main",
        ],
    },
    package_data={
        "heinrich": [
            "knowledge/*.yaml",
            "knowledge/*.json",
            "knowledge/*.csv",
        ],
    },
    include_package_data=True,
    keywords=[
        "TRIZ",
        "innovation",
        "problem-solving",
        "artificial-intelligence",
        "engineering",
        "systematic-innovation",
        "inventive-principles",
        "contradiction-matrix",
    ],
    project_urls={
        "Documentation": "https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/docs",
        "Source": "https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine",
        "Tracker": "https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/issues",
    },
)
