from setuptools import setup, find_packages

# Read requirements safely
with open('requirements.txt', 'r') as file:
    requirements = [
        line.strip() for line in file
        if line.strip() and not line.strip().startswith('#')
    ]

# Read README for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="summarize",
    version="0.0.1",
    author="Kamran Khan",
    author_email="kamrankhnkami@gmail.com",
    description="Demo Python CLI tool to summarize text using HuggingFace Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamipakistan/packaging_your_project",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            # 👇 Corrected: no `.py` in module path
            "summarize=HuggingfaceSummarization.main:main",
        ],
    },
    include_package_data=True,  # ensures data files are included if specified in MANIFEST.in
)
