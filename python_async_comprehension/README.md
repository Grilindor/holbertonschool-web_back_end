# Python Asynchronous Comprehension

## Project Overview

This project is focused on understanding and implementing asynchronous programming concepts in Python, specifically using asynchronous generators and comprehensions. The goal is to create simple but powerful examples that demonstrate how to work with asynchronous code efficiently.

## Learning Objectives

By the end of this project, you will be able to:

- Write an asynchronous generator.
- Use asynchronous comprehensions.
- Type-annotate generators in Python.

## Requirements

- **Python Version**: The code is written in Python 3.7 and should be executed using this version.
- **Style Guide**: The code adheres to the `pycodestyle` style guide (version 2.5.x).
- **Documentation**: All modules and functions include documentation explaining their purpose and usage.

## Tasks

### Task 0: Async Generator

Write a coroutine called `async_generator` that takes no arguments.

- The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yield a random number between 0 and 10.
- Use the `random` module to generate random numbers.

**File:** `0-async_generator.py`

### Task 1: Async Comprehensions

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

- The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

**File:** `1-async_comprehension.py`

### Task 2: Run Time for Four Parallel Comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

- `measure_runtime` should measure the total runtime and return it.
- Notice that the total runtime is roughly 10 seconds, which is because the tasks run concurrently.

**File:** `2-measure_runtime.py`

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/holbertonschool-web_back_end
    cd python_async_comprehension
    ```

2. Run the Python files:

    ```bash
    python3 0-async_generator.py
    python3 1-async_comprehension.py
    python3 2-measure_runtime.py
    ```

## Code Style

This project adheres to the `pycodestyle` (version 2.5.x) style guide. Make sure your code is properly formatted by running:

```bash
pycodestyle your_file.py
```

# Documentation
Ensure all your modules and functions are properly documented:

```bash
python3 -c 'print(__import__("your_module").__doc__)'
python3 -c 'print(__import__("your_module").your_function.__doc__)'
```
