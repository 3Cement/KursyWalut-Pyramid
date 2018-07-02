import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'sqlalchemy',
    'requests',
    'waitress',
    'zope.sqlalchemy',
]

setup(name='kursy',
      version="0.0.1",
      author="Daniel Milewski",
      uthor_email="danielmilewski123@gmail.com",
      description="A small program that synchronizes current currency prices",
      install_requires=requires,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/3Cement/KursyWalut-Pyramid",
      packages=setuptools.find_packages(),
      classifiers=(
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      ),
      entry_points="""\
      [paste.app_factory]
      main = kursy:main
      [console_scripts]
      initialize_kursy_db = kursy.initialize_db:main
      """,
)