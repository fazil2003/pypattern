# pypattern 0.0.3

<p align="center">
  <img src="./assets/images/logo.png" style='width: 30%;'/>
</p>
<br /><br />

Python library to print the characters, numbers as pattern.
<br /><br />


## 🌟 Directories
💫 capital_letters <br />
💫 numbers <br />
💫 small_letters <br />
💫 special_characters <br />
<br />

## 🌟 How to install
💫 Go to your command prompt and type the following command.
```
pip install pypattern
```
<br />

## 🌟 How to use
💫 Import the library in your project
```python
import pypattern
```

💫 Send the text as argument in the ```pattern()``` that you want to print as pattern.
```python
pypattern.pattern('Hello World')
```

💫 This will print the text as pattern in the console. <br />
<br />


## 🌟 How to build and upload to PyPI
💫 Source Distribution
```
pip install setuptools twine
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
💫 Wheel File
```
pip install setuptools wheel
python setup.py bdist_wheel
twine upload dist/*
```