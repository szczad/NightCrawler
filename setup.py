#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.2019 17:34

from setuptools import setup


def readme():
    with open('README.rst', 'r') as f:
        return f.read()


setup(
    name='NightCrawler',
    version='0.1dev1',
    description='Website crawling bot',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.2',
    ],
    keywords='crawler spider website',
    url='https://github.com/szczad/NightCrawler',
    author='Grzeoorz Szczudlik',
    author_email='2914011+szczad@users.noreply.github.com',
    license='MIT',
    packages=['nightcrawler'],
    install_requires=[
        'beautifulsoup4',
        'request'
    ],
    entry_points={
        'console_scripts': [
            'nightcrawler = nightcrawler.crawler:main'
        ]
    }
)