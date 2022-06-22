from setuptools import setup, find_packages
import os

version = '0.3'

long_description = (
    open('README.txt').read())

setup(name='hs.admin.api',
      version=version,
      description="Hostsharing HSAdmin API",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Hostsharing HSAdmin API',
      author='Hostsharing eG',
      author_email='info@hostsharing.net',
      url='https://www.hostsharing.net',
      license='lgpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['hs', 'hs.admin'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'requests',
          'pyyaml',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
