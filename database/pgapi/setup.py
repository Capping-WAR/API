#!/usr/bin/python3
# Daniel Nicolas Gisolfi

from setuptools import find_packages
from setuptools import setup

setup(
	name='pgapi',
	version='1.0.0',
	description=(
		'An abstracted Postgres API for the War DB'
	),
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/Capping-WAR/API/tree/master/database/pgapi',
	author='dgisolfi',
	license='MIT',
	packages=find_packages(),
   
	install_requires=[
        'psycopg2 >= 2.8.3'
    ],
	zip_safe=False,
)