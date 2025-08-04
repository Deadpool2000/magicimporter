from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="magicimporter",
    version="0.1.0",
    author="Salil",
    author_email="d2kyt@protonmail.com",
    description="Smart Python import wrapper with lazy load and auto-install",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deadpool2000/magicimporter",
    project_urls={
        "Documentation": "https://github.com/Deadpool2000/magicimporter#readme",
        "Source": "https://github.com/Deadpool2000/magicimporter",
        "Issues": "https://github.com/Deadpool2000/magicimporter/issues",
    },
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="import lazy pip auto-install utility dev-tools",
    license="MIT",

)
