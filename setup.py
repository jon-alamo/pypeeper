import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pypeeper',
    version='0.2',
    author="Jonatan Rivilla Alamo",
    author_email="jonrivala@gmail.com",
    description=(
        "A minimalist, single-threaded and broadcast-routed observable "
        "pattern."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rolandshoemaker/py-peeper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
 )
