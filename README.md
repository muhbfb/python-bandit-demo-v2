![ Bandit Logo](https://raw.githubusercontent.com/pycqa/bandit/main/logo/logotype-sm.png)
======
![ Bandit Build](https://github.com/PyCQA/bandit/actions/workflows/pythonpackage.yml/badge.svg?branch=main)
![ Bandit docs](https://readthedocs.org/projects/bandit/badge/?version=latest)
![ Bandit py version](https://img.shields.io/pypi/pyversions/bandit.svg)

# 🔐 Python Bandit SAST Demo

This is a simple Python project that demonstrates how to use **Bandit**, a Static Application Security Testing (SAST) tool for Python.

## 📦 What’s Inside

- `vulnerable_app.py`: Example with a command injection vulnerability
- `secure_app.py`: Safer refactored version
- `.github/workflows/security.yml`: GitHub Actions config for automated scanning

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Sergio-Colque-Ponce/python-bandit-demo.git
cd python-bandit-demo
```

### 2. Install Bandit

```bash
pip install bandit
```

### 3. Run Bandit on the vulnerable code

```bash
bandit -r vulnerable_app.py
```

### 4. Run Bandit on the secure version

```bash
bandit -r secure_app.py
```

## 🤖 GitHub Actions Integration

This repo includes a GitHub Actions workflow that automatically scans your code on every push or pull request using Bandit.

## 🎥 Video

👉 [Watch the video explanation over 5-min here](https://tiktok.com)

## 🛡️📄 About Bandit

Bandit is a tool designed to find common security issues in Python code by scanning abstract syntax trees (ASTs). It’s simple to use and perfect for DevSecOps pipelines.

[Bandit GitHub Repository](https://github.com/PyCQA/bandit/tree/main)

> Created by the OpenStack Security Group