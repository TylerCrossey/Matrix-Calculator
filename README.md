# Matrix Calculator

An interactive command-line matrix calculator written in Python. It performs row operations, row reduction (Gauss-Jordan elimination), and inversion using exact fractions, so results like 1/3 stay exact instead of turning into floating-point approximations.

## Features

- Exact rational arithmetic with Python's `fractions.Fraction`
- Elementary row operations: swap, scale, and add a multiple of one row to another
- Reduced row echelon form (`rref`) of any matrix, including rank-deficient ones
- Matrix inverse, with a clear error for singular matrices
- Interactive shell with named matrices, built-in help, and error messages instead of crashes
- Unit tests with pytest

## Quick start

Requires Python 3.10 or newer.

```bash
git clone https://github.com/TylerCrossey/Matrix-Calculator.git
cd matrix-calculator
pip install -r requirements.txt   # only needed for the tests
python main.py
```

Run the tests:

```bash
pytest
```

## Example session

```
matrix> set A 1,2;3,4
Stored matrix A as:
1  2
3  4
matrix> rref A
1  0
0  1
matrix> swap A 1 2
Updated matrix A is:
3  4
1  2
matrix> show A
3  4
1  2
matrix> set B 1/2,1;4,5
Stored matrix B as:
1/2  1
4  5
matrix> inv B
-10/3  2/3
8/3  -1/3
matrix> scale B 1 2
Updated matrix B is:
1  2
4  5
matrix> mul C A B
Updated matrix C is:
19  26
9  12
matrix> show C
19  26
9  12
```

## Entering matrices

Rows are separated by `;` and entries by `,`. Entries can be integers, fractions, or decimals, and all are converted to exact fractions:

```
set A 1,1/2;3,4
set B 0.5,2;1,-3/4
```

All rows must have the same number of entries. Row numbers in commands start at 1.

## Commands

| Command | What it does |
|---------|--------------|
| `set NAME MATRIX` | store a matrix, e.g. `set A 1,2;3,4` |
| `show NAME` | print a stored matrix |
| `swap NAME ROW1 ROW2` | swap two rows |
| `scale NAME ROW FACTOR` | multiply a row by a nonzero factor, e.g. `scale A 1 1/2` |
| `add NAME TARGET SOURCE FACTOR` | add FACTOR times the SOURCE row to the TARGET row |
| `rref NAME` | print the reduced row echelon form |
| `inv NAME` | print the inverse of a square matrix |
| `help` / `help COMMAND` | list commands or show usage for one |
| `quit` / `exit` / Ctrl-D | leave the shell |

## Project structure

```
matrix-calculator/
├── main.py                 # entry point, starts the shell
├── shell.py                # interactive shell (cmd.Cmd): parsing, commands, error handling
├── matrix_operations.py    # row operations, row_reduce, inverse
├── test_matrix_tools.py    # pytest tests
├── requirements.txt
└── README.md
```

## Design notes

- **Exact arithmetic.** Every entry is a `Fraction`, so elimination never loses precision. Floating point would turn `1/3` into `0.3333...` and make "is this entry zero?" checks unreliable.
- **Inverse by augmentation.** `inverse` row-reduces `[A | I]`. If the left half becomes the identity, the right half is the inverse. Otherwise the matrix is singular and a `ValueError` is raised.
- **Errors in one place.** The shell catches `KeyError`, `ValueError`, and `ZeroDivisionError` in `onecmd`, so a bad command prints a message and the session keeps going.

## Limitations and roadmap

- Matrices are plain lists of lists, with no size limit and no optimization, so this is meant for small matrices.
- Planned: determinant, rank, solving linear systems `Ax = b`, and loading matrices from a file.
