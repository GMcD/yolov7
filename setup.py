import site
from pathlib import Path
import json
from setuptools import setup, find_packages


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

def version():
    """get version from package.json"""
    package_dir = Path(__file__).parent.absolute()
    with open(f"{package_dir}/package.json") as jsf:
        data = json.load(jsf)
    return data["version"]


PYTHON_VERSION = "3.8"

VERSION = version()

PACKAGES = find_packages(where="src")

LIBS = site.getsitepackages()

setup(
    name="yolov7",
    version=VERSION,
    description="YoloV7 module",
    long_description=open("README.md").read(),
    author="Gary MacDonald",
    author_email="gary.macdonald@projectscapa.com",
    url="https://www.projectscapa.com",
    license="ISC",
    install_requires=parse_requirements("./requirements.txt"),
    package_dir={"": "."},
    packages=PACKAGES,
    include_package_data=True,
    # Pop packaged files into data dir under virtualenv, for now
    data_files=[
        (
            "data",
            [
                "package.json",
                "README.md",
                "requirements.txt",
            ],
        ),
    ],
)
