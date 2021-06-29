import os
import sys

sys.path.append ('pyact')
import __base__

from setuptools import setup

def read (*paths):
	with open (os.path.join (*paths), 'r') as aFile:
		return aFile.read()

setup (
	name = 'Pyact',
	version = __base__.pa_version,
	description = 'A React API for Transcrypt',
	long_description = (
		read ('README.rst') + '\n\n' +
		read ('pyact/license_reference.txt')
	),
	keywords = ['transcrypt', 'react', 'python', 'browser'],
	url = 'https://github.com/QQuick/Pyact',	
	license = 'Apache 2.0',
	author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
	packages = ['pyact'],
	install_requires = [
		'transcrypt'
	],
	include_package_data = True,
	classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.9',
	],
)
