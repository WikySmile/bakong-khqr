from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
readme = Path(__file__).parent / "README.md"
long_description = readme.read_text()

setup(
    name="bakong-khqr",
    version="0.1.0",
    author="BAN Sothen",
    author_email="bansokthen@gmail.com",
    description="A Python library for generating QR codes for transactions compliant with the Bakong KHQR standard. (Unofficial NBC Library)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsthen/bakong-khqr",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
)
