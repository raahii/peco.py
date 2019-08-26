from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="peco",
    version="0.0.1",
    description="",
    long_description=readme,
    author="Yuki Nakahira",
    author_email="piyo56.net@gmail.com",
    install_requires=["prompt-toolkit==2.0.9"],
    url="https://github.com/raahii/peco.py",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
