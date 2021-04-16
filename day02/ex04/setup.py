import setuptools

setuptools.setup(
    name="ai42",
    version="0.0.1",
    author="rofernan",
    author_email="rofernan@student.42.fr",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)