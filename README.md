<p align="center">
Stringpath for treating a string as a path
</p>

<p align="center">
<a><img src="https://img.shields.io/badge/version-1.0.0-blue"></a>
<a><img src="https://img.shields.io/badge/docs-passing-brightgreen.svg"></a>
<a><img src="https://img.shields.io/github/license/PascalVallaster/background-changer"></a>
</p>


## About stringpath

**stringpath** is a python script for simulating the 'cd' command on a string that contains a path.

<p style="color:orange" align="center">
Please report errors directly to my email: <a href="mailto:pascalvallaster@gmail.com?subject=Issue/Bug">pascalvallaster@gmail.com</a>
<p>


---


## Install

### Download:

Download with `pip`:

```term
pip install stringpath
```

or download the `Source Distribution` and, or `Built Distribution` under `Download Files`.

### Install dependencies:

- Python 3.4^
  - Standard Library


---


## Usage

### Basic usage example

```python
from stringpath import change_directory

cwd = r"C:\my/current\path"
cd = r"..\i/want\to\cd/in/here"
new_cwd = change_directory(cwd, cd)
```
For more usage details see the docs in the functions itself


### Use Case example

Imagine your program has to execute sys-commands in different (user-depending) directories with _subprocess_ which will be determined by 
the user using the command 'cd'. The problem is, you don't want to change the current working directory 
in order to avoid problems and security threats. This tool allows you to accomplice that.

Example:
```python
import subprocess
import stringpath

command = "dir"
cwd = "C:/MyFiles/MyAppFolder/"
print("'cd' into a different location")
cd = input(cwd + ">")
cwd = stringpath.change_directory(cwd, cd)
subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd)
```


---


## Uninstall

```term
pip uninstall stringpath
```