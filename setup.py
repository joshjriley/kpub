#!/usr/bin/env python
from setuptools import setup


# PyPi requires reStructuredText instead of Markdown,
# so we convert our Markdown README for the long description
try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

# Command-line tools
entry_points = {'console_scripts': [
    'kpub = kpub:kpub',
    'kpub-update = kpub:kpub_update',
    'kpub-add = kpub:kpub_add',
    'kpub-delete = kpub:kpub_delete',
    'kpub-import = kpub:kpub_import',
    'kpub-export = kpub:kpub_export',
    'kpub-plot = kpub:kpub_plot',
    'kpub-spreadsheet = kpub:kpub_spreadsheet'
]}

setup(name='kpub',
      version='2.0.0dev',
      description="A simple tool to keep track of the ADS publications "
                  "related to a particular mission.",
      long_description=long_description,
      author='Geert Barentsen (original), Josh Riley (v2.0 generic model)',
      author_email='hello@geert.io, joshjriley@gmail.com',
      license='MIT',
      url='http://github.com/joshjriley/kpub',
      packages=['kpub'],
      data_files=[('kpub/config', ['kpub/config/config.live.yaml']),  
                  ('kpub/templates', ['kpub/templates/template.md', 'kpub/templates/template-overview.md'])],
      install_requires=["jinja2",
                        "six",
                        "astropy",
                        "textract"],
      entry_points=entry_points,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          ],
      )
