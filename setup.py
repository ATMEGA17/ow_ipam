import os

from setuptools import find_packages, setup

from openwisp_ipam import get_version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        if line.startswith('#') or line == '' or line.startswith('git'):
            continue
        requirements.append(line)
    return requirements


setup(

)
