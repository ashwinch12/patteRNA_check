"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from os.path import join
from setuptools import find_packages
from setuptools import setup

from src.patteRNA.version import __version__

# Get the long description from the README file
with open(join("README.md")) as f:
    long_description = f.read()

setup(
    name="patteRNA",
    version=__version__,
    description="Rapid mining of RNA secondary structure motifs from profiling data.",
    long_description=long_description,
    url="https://github.com/ashwinch12/patteRNA_check",
    author="Ashwin Amalaruban",
    author_email="ashm@ucdavis.edu",
    license="BSD-2",
    keywords="RNA structure mining",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3 :: Only"
    ],

    # Python requirements
    python_requires=">=3",

    # Specify source packages
    packages=find_packages('src'),
    package_dir={'': 'src'},

    # Dependencies
    install_requires=[
        "exrex",
        "humanfriendly",
        "numpy",
        "matplotlib",
        "tqdm",
        "scikit-learn",
        "scipy",
    ],

    # Include data files
    package_data={
        "sample_data": ["sample_data/*"],
    },

    # Create the executable
    entry_points={
        'console_scripts': [
            'patteRNA = patteRNA.cli:main'
        ]
    },

    zip_safe=False
)
