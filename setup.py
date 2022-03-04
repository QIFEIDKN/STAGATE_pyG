from setuptools import Command, find_packages, setup

__lib_name__ = "STAGATE_pyG"
__lib_version__ = "1.0.0"
__description__ = "Deciphering spatial domains from spatially resolved transcriptomics with adaptive graph attention auto-encoder"
__url__ = "https://github.com/QIFEIDKN/STAGATE"
__author__ = "Kangning Dong"
__author_email__ = "dongkangning16@mails.ucas.ac.cn"
__license__ = "MIT"
__keywords__ = ["spatial transcriptomics", "Deep learning", "Graph attention auto-encoder"]
__requires__ = ["requests",]

with open("README.rst", "r", encoding="utf-8") as f:
    __long_description__ = f.read()

setup(
    name = __lib_name__,
    version = __lib_version__,
    description = __description__,
    url = __url__,
    author = __author__,
    author_email = __author_email__,
    license = __license__,
    packages = ['STAGATE_pyG'],
    install_requires = __requires__,
    zip_safe = False,
    include_package_data = True,
    long_description = __long_description__
)
