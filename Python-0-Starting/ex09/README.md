# ft_package

A small example Python package for the Piscine Python 0 exercise 09.

1. Build the package from the project root:

```sh
python3 -m build
```

This creates the `dist/` directory containing a source distribution (`.tar.gz`) and a wheel (`.whl`).

4. Install the built:

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Test the package

The `test.py` file exercises the `count_in_list` function. Run it from the same directory:

```sh
python3 test.py
```

Expected output:

```text
2
0
```
