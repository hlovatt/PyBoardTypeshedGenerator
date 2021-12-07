# Micropython Typeshed Generator (formerly known as PyBoard Typeshed Generator)

Code to generate typesheds (type hint interface stubs `.pyi`) from restructured text help files (`.rst`) as used in
[MicroPython](http://micropython.org). 
This code generates the typesheds in
[PyBoardTypeshed](https://github.com/hlovatt/PyBoardTypeshed)
repository. The `README` for the typeshed
[repository](https://github.com/hlovatt/PyBoardTypeshed)
describes how to use the typesheds.

See doc comment in `rsi2pyi.py` for a *brief* description of how to write translators.

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
