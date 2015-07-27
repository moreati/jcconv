# -*- coding: utf-8 -*-
from setuptools import setup
import os

## Get long_description from index.txt:
f = open(os.path.join('README.rst'))
long_description = f.read().strip()
f.close()


if __name__ == '__main__':
  # build distribution package
  setup(
    packages         = ('jcconv',),
    name             = 'jcconv',
    version          = '0.2.3',
    description      = 'jcconv "JapaneseCharacterCONVerter", interconvert hiragana, katakana, halfwidth kana',
    long_description = long_description,
    author           = 'Matsumoto Taichi',
    author_email     = 'taichino@gmail.com',
    url              = 'http://github.com/taichino/jcconv',
    keywords         = 'japanese converter, hiragana, katakana, half-width kana',
    license          = 'MIT License',
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: POSIX",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"],
    tests_require = ['six'],
    test_suite = "jcconv.jcconv_test",
    install_requires = ['six'],
    )
