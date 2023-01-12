from setuptools import setup
from os import path


current_dir = path.abspath(path.dirname(__file__))


with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(current_dir, 'requirements.txt'), 'r') as f:
    install_requires = f.read().split('\n')


setup(
    name='uci_dataset',
    version='0.0.7',
    author='Project Lightning',
    author_email='aryam.bahrami@yahoo.ca',
    packages=['uci_dataset'],
    url='https://github.com/ProjectLightningDev/web.py',
    license='Boost Software License 1.0',
    description='Read dataset without the need to download any file from an external website.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires='numpy',
    install_requires=install_requires,
    keywords='uci dataset, toy dataset, public dataset',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Boost Software License 1.0 License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)
