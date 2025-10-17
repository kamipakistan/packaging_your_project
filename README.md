# Huggingface Summarization CLI Tool

A lightweight and educational **Python CLI tool** built with **Click** and **HuggingFace Transformers**, designed to summarize text or URLs quickly from your terminal.

---

## Features

* Summarize text from files or live URLs  
* Built with modern Python packaging tools (`setuptools`)  
* Uses HuggingFace `transformers` for NLP  
* Clean command-line interface powered by `Click`  
* Easy to package, distribute, or extend  

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/kamipakistan/packaging_your_project.git
cd packaging_your_project
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # Linux / macOS
# OR
.venv\Scripts\activate        # Windows
```

### 3. Production / Distribution (Built Package Install)
```bash
pip install dist/summarize-0.0.1-py3-none-any.whl
```

### 4. Usage
Summarize text from a local file
```bash
summarize --file HuggingfaceSummarization/data/mlops-wikipedia.txt
```
Summarize text directly from a URL
```
summarize --url https://en.wikipedia.org/wiki/MLOps
```

Example Output
```
Summarization process complete!
================================================================================
Machine learning is a subset of artificial intelligence focused on building
systems that learn from data. It powers applications like image recognition,
speech processing, and predictive analytics.
```

## Development Notes

This project is structured as a Python package, so it can be installed, tested, and distributed easily.

### Editable (Development) Installation

Use the following command to install your project in “editable” mode — this means any code changes you make will immediately reflect in the CLI tool:
```
pip install -e .
```
### Add a New CLI Command

You can extend functionality easily by adding a new command in `main.py`:
```python
@click.command()
@click.option('--text', help='Text to summarize')
def summarize_text(text):
    click.echo(process(text))
```



Then add it to your `entry_points` in `setup.py` if you want a new command name:
```python
entry_points={
    "console_scripts": [
        "summarize=HuggingfaceSummarization.main:main",
        "summarize-text=HuggingfaceSummarization.main:summarize_text"
    ],
},
```

### Run the CLI locally without installing
```python
python -m HuggingfaceSummarization.main --file HuggingfaceSummarization/data/mlops-wikipedia.txt
```

### Project Structure
```arduino
PackagingYourProject/
│
├── HuggingfaceSummarization/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── data/
│   └── mlops-wikipedia.txt
│
├── setup.py
├── requirements.txt
└── README.md
```

### Build & Distribution

To build your distributable `.tar.gz` and `.whl` files:
```bash
python setup.py sdist bdist_wheel
```

You’ll find your build artifacts inside the `/dist` folder.

To upload them to PyPI, install **twine** and run:
```bash
pip install twine
twine upload dist/*
```


### Uninstall

If you want to remove the package:
```bash 
pip uninstall summarize -y
```


### Author
**Kamran Khan**  
**kamrankhnkami@gmail.com**  
[GitHub Profile](https://github.com/kamipakistan)

### License
This project is licensed under the MIT License — feel free to modify and use it for learning, research, or production purposes.