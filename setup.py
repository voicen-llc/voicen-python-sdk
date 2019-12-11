#!/usr/bin/env python

from glob import glob
from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession
import re
import ast
import os

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/voicen/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("README.md", "r") as fh:
	long_description = fh.read()

parsed_requirements = parse_requirements(
    'requirements.txt',
    session=PipSession())

requirements = [str(ir.req) for ir in parsed_requirements]

setup(
    name="voicen", # Replace with your own username
    version="1.0.0",
    author="Voicen LLC",
    author_email="info@voicen.com",
    description="The python SDK developed by Voicen allows customers to use speech-to-text service of Voicen.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voicen-llc/voicen-python-sdk",
    packages=find_packages("src"),
		package_dir={'': 'src'},
		py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob('src/*.py')],
		include_package_data=True,
		install_requires=requirements,
		zip_safe=False,
		license='MIT license',
		keywords='voicen',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
