"""
setup.py
"""
# vim:fileencoding=utf-8
# Copyright -2018 (c) Teso group
# See also LICENSE.txt

from setuptools import setup, find_packages


setup(
    name='pymn_address',
    version='0.0.0',
    author='Erdenezul Batmunkh',
    author_email='erdenezul@shine.mn',
    description='City, Ditrict, Province, sum'
                'definitions and their translations',
    long_description=(
        open('README').read() + '\n' +
        open('HISTORY.txt').read()),
    license='LGPL 2.1',
    keywords='mongolia address library',
    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
    ],
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'}
)
