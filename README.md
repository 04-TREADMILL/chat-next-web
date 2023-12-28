# Chat Next Web

Build comprehensive chat frontend web page powered by Streamlit 🚀

[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## setup

After cloning this project, please proceed with the following initialization:

```bash
pip install -r requirements.txt
pre-commit install
```

Regenerate the requirements:

```bash
python -m pip freeze --all > requirements.txt
```

> TODO: clean unused requirements

## run

```bash
streamlit run main.py
```

## config

The default username and password are both set to `admin`.
