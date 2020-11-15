"""
 Created by Narayan Schuetz at 15.11.20 
 University of Bern
 
 This file is subject to the terms and conditions defined in
 file 'LICENSE.txt', which is part of this source code package.
"""


from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pandas_normalization",
    version="0.0.1",
    author="Narayan Schuetz",
    author_email="narayan.schuetz(at)artorg.unibe.ch",
    description="Monkey patches pandas to directly allow data normalization by means of min-max scaling and zero-mean "
                "unit-variance standardization unit variance This is only for convenience as I found myself too often "
                "having to write this by hand or use sklearn, which both leads to less concise code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NarayanSchuetz/pandas_normalization.git",
    packages=find_packages(),
    install_requires=[
        "markdown==3.0.1",
        "pandas"
    ],  # has been tested with pandas 1.1.3 and Python 3.8
    test_suite='nose.collector',
    tests_require=['nose', "pandas", "numpy"],
    zip_safe=False,
    python_requires='>=3.6'
)
