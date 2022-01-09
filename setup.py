from setuptools import setup, find_packages
from distutils.command.build import build

from wagtailiconify import __version__

class NPMInstall(build):
    def run(self):
        self.run_command("npm install")
        self.run_command("npm build")
        build.run(self)

setup(
    name='wagtailiconify',
    version=__version__,
    description='A plugin for Wagtail CMS, icon blocks (fontawesome)',
    author='Nefonfo',
    author_email='victorarmenta30@gmail.com',
    url='https://github.com/Nefonfo/wagtailiconify',
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=2.15.0",
        "Django>=3.2.0",
    ],
    cmdclass={
        'npm_install': NPMInstall
    },
)