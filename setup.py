#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="pig",
	version="0.1",
	description="Test for pip install git+",
	url="https://github.com/trsqxyz/pig",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	pig = pig.pig:main
	""",
	)
