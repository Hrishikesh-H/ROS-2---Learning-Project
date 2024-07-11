from setuptools import find_packages
from setuptools import setup

setup(
    name='hh_tt_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('hh_tt_interfaces', 'hh_tt_interfaces.*')),
)
