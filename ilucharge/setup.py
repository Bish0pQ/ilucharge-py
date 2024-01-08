from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ilucharge_bish0pq",
    version="0.0.1",
    author="Tommy Versantvoort",
    author_email="ilucharge-pack@nodata4you.mozmail.com",
    description="A small package to work with EV charges of the company ILumen, uses existing ILucharge API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bish0pQ/ilucharge-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)