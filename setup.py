from setuptools import setup

version = '0.0.1'

setup(name="helga-fredoisms",
      version=version,
      description='Helga plugin for saying things alfredo might say',
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
      py_modules=['helga_fredoisms'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'helga_handlers': [
              'fredoisms = helga_fredoisms:FredoismExtension',
          ]
      },
)
