#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='nordpool',
    version='0.3.4',
    description='Python library for fetching Nord Pool spot prices.',
    author='Kimmo Huoman / Aleksander Veksler',
    author_email='aleksve@gmail.com',
    url='https://github.com/aleksve/nordpool',
    packages=[
        'nordpool',
    ],
    install_requires=[
        'python-dateutil>=2.6.1',
        'pytz>=2017.2',
        'requests>=2.18.4',
    ])
