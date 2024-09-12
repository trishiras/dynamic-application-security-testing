from setuptools import setup, find_packages
from dynamic_application_security_testing.__version__ import __version__


setup(
    name="dynamic_application_security_testing",
    version=__version__,
    author="sumit",
    author_email="sumit@mail.com",
    description="dynamic-application-security-testing",
    long_description=open("README.md").read(),
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "dynamic_application_security_testing=dynamic_application_security_testing.main:main",
        ],
    },
)
