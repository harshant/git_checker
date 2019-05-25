<h4 align="center">Tool to check accessibility of .git file</h4>

<p align="center">
  <a>
  <img src="https://img.shields.io/badge/License-GPL%20v2-blue.svg">
  </a>
  <a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
</p>
<p align="center">
<img src="https://i.ibb.co/t3TFLxq/git-checker.png" alt="git-checker" border="0"></a>
</p>


This tool is one of the two challenges of grofers hiring process, emphasis is given on structuring of this project and code style.
This code follows Black code style and is PEP8 compliant.

### Installing Requirements
> pip3 install -r requirements.txt

### Usage 
> python3 git_checker -i /path/to/file.txt

usage: git_checker.py [-h] [-i INPUT]

optional arguments:
  -h, --help                    show this help message and exit
  -i INPUT, --input INPUT       Input a relative file path containing list of domain names
