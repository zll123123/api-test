from setuptools import setup, find_packages

requirements = []

setup(
    name="unitest2",
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "unitest2 = unitest2.main:main",
        ]
    },
)
