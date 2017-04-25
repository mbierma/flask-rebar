#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

found_packages = find_packages(where=".")
packages = ["%s" % package for package in found_packages]

if __name__ == '__main__':
    setup(
        author='PlanGrid',
        description='Tools for quickly getting a Flask service up and running',
        name='flask-toolbox',
        packages=packages,
        install_requires=[
            'bugsnag[flask]==3.1.0',
            'Flask==0.12.1',
            'marshmallow==2.13.5'
        ],
        version='0.0.1',
        zip_safe=True,
        url='https://github.com/plangrid/flask-toolbox'
    )
