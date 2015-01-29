from setuptools import setup  # , find_packages

setup(
    name='pychdk',
    version='0.1',
    author='David Manouchehri',
    author_email='david@davidmanouchehri.com',
    description='Python module for controlling CHDK cameras through USB PTP.',
    url="https://github.com/Manouchehri/pychdk",
    # long_description=__doc__,
    packages=['ptp2'],
    license = "GPLv3",
    # include_package_data=True,
    zip_safe=True,
    install_requires=['pyusb'],
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3.4',
                 'Topic :: Software Development :: Libraries', 'Topic :: Utilities']
)