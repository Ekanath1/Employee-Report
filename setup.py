from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nextreport/__init__.py
from nextreport import __version__ as version

setup(
	name="nextreport",
	version=version,
	description="All print format in one report",
	author="eknath",
	author_email="eknath@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
