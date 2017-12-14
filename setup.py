#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup for matplotlib tester."""

from setuptools import setup

INSTALL_REQUIRES = [
    'setuptools',
    'numpy == 1.12.1',
    'matplotlib == 2.1.1',
]

SETUP_REQUIRES = [
    'pytest-runner',
]

TEST_REQUIRES = [
    'pytest',
]

setup(name='matplot-tester',
      version='0.1.0',
      description='Test code to show use of the matplotlib python library.',
      url="http://github.com/carlwilson/matplot-tester",
      author='Carl Wilson',
      author_email='carl@openpreservation.org',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,
      tests_require=TEST_REQUIRES,
      packages=['sinplt'],
      test_suite='test',
     )
