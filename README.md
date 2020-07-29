# PyBoardTypeshedGenerator

Code to generate typesheds (type hint interface stubs `.pyi`) from 
restructured text help files (`.rst`) as used in MicroPython.
This code generates the typesheds in repository 
[https://github.com/hlovatt/PyBoardTypeshed]().

See doc comment in `typeshed.py` for a very brief description of 
how to write translators.

Run:
```bash
    cd <directory of PyBoardTypeShedGenerator>
    python3 main.py <destination directory>
```
or if `main.py` is executable:
```bash
    cd <directory of PyBoardTypeShedGenerator>
    ./main.py <destination directory>
```
