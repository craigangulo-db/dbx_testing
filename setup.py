from setuptools import find_packages, setup
from dbx_testing import __version__

setup(
    name="dbx_testing",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
