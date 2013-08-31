try:
	from setuptools.core import setup
except ImportError:
	from distutils.core import setup

setup(
	name='msgpack-tool',
	version='0.0.1',
	author='Feng Zhou',
	packages=['msgpack_tool'],
	url='https://github.com/zweifisch/msgpack-tool',
	description='a cli utility for msgpack/json conversion',
	author_email='zf.pascal@gmail.com',
	install_requires=['msgpack-python'],
	entry_points={
		'console_scripts': ['msgpack=msgpack_tool:main'],
	},
)
