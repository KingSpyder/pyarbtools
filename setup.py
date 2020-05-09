from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('docs\HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Morgan Allison",
    author_email='morgan.allison@keysight.com',
    classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Natural Language :: English',
        'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', ],
    description="PyArbTools provides waveform creation and remote instrument control capabilities for Keysight signal generators.",
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['numpy', 'scipy', 'socketscpi', 'matplotlib'],
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='PyArbTools',
    name='PyArbTools',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/morgan-at-keysight/pyarbtools',
    version='2020.04.0',
    zip_safe=False,
    # name='pyarbtools',
    # version='0.0.14.1',
    # author='Morgan Allison',
    # classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Developers',
    #     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Natural Language :: English',
    #     'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', ],
    # author_email='morgan.allison@keysight.com',
    # description='Signal generator control for Keysight equipment.',
    # long_description=readme + '\n\n' + history,
    # url='https://github.com/morgan-at-keysight/pyarbtools',
    # packages=find_packages(exclude=['docs', 'tests']),
    # install_requires=['numpy', 'scipy'],
    # # package_data={'pyarbtools':['package_data.dat']}
    # license='GPL 3',
)
