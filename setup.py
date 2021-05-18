from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='discretegeom',
    version='0.0.1',
    description='Templates for netCDF discrete geometry files (CF Conventions)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nicholas512/discretegeom',
    author='Nick Brown',
    author_email='nick.brown@carleton.ca',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='data',
    packages=["discretegeom"],
    python_requires='>=3.6',
    install_requires=['pandas', 'netCDF4']
)