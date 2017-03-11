# -*- coding: utf-8 -*-

import unittest

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()


def vcr_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name='vcr',
    version='0.0.1',
    description='Decorator for capturing and simulating network communication',
    long_description=readme,
    author='The ObsPy Development Team',
    author_email='devs@obspy.org',
    url='https://github.com/obspy/vcr',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='setup.vcr_test_suite',
)

