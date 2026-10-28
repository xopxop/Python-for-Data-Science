# Python-1-Array

Introduction to NumPy arrays and image manipulation, part of the
Python for Data Science curriculum.

## Contents

| Exercise | Directory | Description |
| --- | --- | --- |
| ex00 | `ex00/` | `give_bmi` computes BMI from height/weight lists, `apply_limit` flags values above a limit. |
| ex01 | `ex01/` | `slice_me` slices a 2D list as a NumPy array and prints the old/new shapes. |
| ex02 | `ex02/` | `ft_load` loads an image with Pillow, prints its shape and returns it as a NumPy array. |
| ex03 | `ex03/` | `zoom.py` crops the center 400x400 pixels, converts it to grayscale and displays it. |
| ex04 | `ex04/` | `rotate.py` crops the center of the image, transposes it with a manual loop (no NumPy transpose helpers) and displays the grayscale result. |
| ex05 | `ex05/` | `pimp_image.py` applies invert, red, green, blue and grey filters to an image and displays each result. |

Each exercise directory is self-contained and ships its own `load_image.py`
helper plus the image it needs.

## Requirements

- Python 3.10 or newer (this project was developed with Python 3.15.1)
- NumPy
- Pillow (PIL)
- flake8 (style checker, used in place of 42's norminette)

## Setup

Create and activate a virtual environment, then install the dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install flake8 numpy pillow
```

In this project, **flake8 is the norminette command**. Link it inside
the venv with one command:

```sh
ln -s flake8 .venv/bin/norminette
```

Since the link lives in `.venv/bin`, every time you activate the venv
the `norminette` command becomes available and runs flake8 instead:

```sh
source .venv/bin/activate
norminette .
```

This venv already contains the link, so the `norminette` command works
as soon as it is activated. If you delete or recreate `.venv/`, run the
command above again.

To leave the virtual environment:

```sh
deactivate
```

## Style checking

Activate the virtual environment, then run norminette (flake8) from the
root of the project:

```sh
source .venv/bin/activate
norminette . --exclude=.venv
```

Run it on a single exercise with:

```sh
norminette ex00
```

flake8 reports PEP 8 style violations and common errors, the same way
norminette reports style errors for C projects.

## Running the exercises

Always run the scripts from inside their own exercise directory, since
the image paths are relative:

```sh
cd ex00 && python tester.py
cd ex01 && python tester.py
cd ex02 && python tester.py
cd ex03 && python zoom.py
cd ex04 && python rotate.py
cd ex05 && python tester.py
```

Exercises `ex03`, `ex04` and `ex05` open the processed images in your
system's default image viewer, so a graphical environment is required.

## Subject

The original assignment is available in `en.subject.pdf`.
