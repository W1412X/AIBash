"""
AIBash 安装配置

Author: github/W1412X
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取 README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ""

setup(
    name="aibash",
    version="0.1.0",
    author="github/W1412X",
    author_email="",
    description="AI-powered shell command generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/W1412X/aibash",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=5.4.1",
        "requests>=2.25.1",
        "urllib3>=1.26.0",
    ],
    entry_points={
        "console_scripts": [
            "aibash=aibash.main:main",
            "aibash-init=aibash.config_init:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

