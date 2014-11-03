#!/usr/bin/env python

import os.path

from distutils.core import setup

setup(
    version='0.1',
    url='https://github.com/nathforge/django-roma',
    name='django-roma',
    description='https://github.com/nathforge/django-roma',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Nathan Reynolds',
    author_email='email@nreynolds.co.uk',
    packages=['roma'],
    package_dir={'': 'src'},
)
