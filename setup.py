#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.4.3'

setup(name='ici',
      version=version,
      description="方便程序员在terminal查询生词的小工具",
      long_description="""方便程序员在terminal查询生词的小工具""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python iciba dictionary terminal',
      author='yuzhe',
      author_email='lazynightz@gmail.com',
      url='https://github.com/Flowerowl/ici',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'termcolor',
      ],
      entry_points={
        'console_scripts':[
            'ici = ici.ici:main'
        ]
      },
)
