from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()
NEWS = open(os.path.join(here, "NEWS.txt")).read()


version = "1.4.1"

install_requires = [
    "typing_extensions"
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(
    name="lkk_log",
    version=version,
    description="",
    long_description=README + "\n\n" + NEWS,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords="",
    author="lkk9898969",
    author_email="",
    url="",
    license="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={"console_scripts": ["lkk_log=lkk_log:main"]},
)
