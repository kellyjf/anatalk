#!/usr/bin/python


from setuptools import setup


setup (
	name='anatalk',
	version='0.1',
	packages=['anatalk'],
	entry_points ={
		'console_scripts':['anatalk=anatalk.__main__:main']
	}
)

