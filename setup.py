#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='web-parsers',
    version='0.0.1',
    description='Simple, extendable HTML and XML data extraction engine using YAML configurations '
                'and some times pythonic functions.',
    author='Ravi Raja Merugu',
    author_email='ravi@invanalabs.ai',
    url='https://github.com/invanalabs/web_parsers',
    packages=find_packages(
        exclude=("dist", "docs", "tests",)
    ),
    install_requires=[
        'parsel>=1.5.2',
        'PyYAML==5.1.2',
        'xmltodict==0.12.0'
    ],
    entry_points={
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Environment :: Console',
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License',  # Again, pick a license
        'Operating System :: POSIX :: Linux',
        'Operating System :: Mac OS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
