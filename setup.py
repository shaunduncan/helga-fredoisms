import os
from setuptools import setup, find_packages

version = '0.0.1'
setupdir = os.path.dirname(os.path.abspath(__file__))
description = open(os.path.join(setupdir, 'README.md'), 'r').read()

setup(name="helga-fredoisms",
      version=version,
      description=description,
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot fredoisms',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/helga-fredoisms',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'helga_handlers': [
              'fredoisms = fredoisms:FredoismExtension',
          ]
      },
)
