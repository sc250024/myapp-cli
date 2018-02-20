from setuptools import find_packages
from setuptools import setup
import os

base_dir = os.path.dirname(__file__)

setup(
    entry_points = '''
        [console_scripts]
        myapp=myapp.main:entry_point
    ''',
    install_requires = [
        'click==6.7'
    ],
    name = "myapp-cli",
    packages=find_packages(),
    setup_requires="setuptools",
    version = "0.1",
)
