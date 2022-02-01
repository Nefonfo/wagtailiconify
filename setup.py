from setuptools import setup, find_packages
from setuptools.command.sdist import sdist as base_sdist
from setuptools.command.bdist_egg import bdist_egg as base_bdist_egg

from distutils.command.build import build
from distutils import log

import subprocess

from wagtailiconify import __version__


with open("README.md", "r") as readme:
    long_description = readme.read()


class assets_mixin:
    def compile_assets(self):
        try:
            subprocess.check_call(["npm", "install"])
            subprocess.check_call(["npm", "run", "build"])
        except (OSError, subprocess.CalledProcessError) as e:
            print("Error compiling assets: " + str(e))
            raise SystemExit(1)


class sdist(base_sdist, assets_mixin):
    def run(self):
        self.compile_assets()
        base_sdist.run(self)


class bdist_egg(base_bdist_egg, assets_mixin):
    def run(self):
        self.compile_assets()
        base_bdist_egg.run(self)


setup(
    name="wagtailiconify",
    version=__version__,
    description="A plugin for Wagtail CMS, icon blocks (fontawesome)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nefonfo",
    author_email="victorarmenta30@gmail.com",
    url="https://github.com/Nefonfo/wagtailiconify",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords=["development", "django", "wagtail"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=2.15.0",
        "Django>=3.2.0",
    ],
    cmdclass={
        "sdist": sdist,
        "bdist_egg": bdist_egg,
    },
)
