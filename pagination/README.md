# Pagination Project

## Project Overview

This project focuses on implementing various pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient pagination. By the end of this project, you will have a solid understanding of how to efficiently paginate datasets, manage large sets of data, and ensure robustness in the face of data modifications.

## Learning Objectives

By the end of this project, you will be able to:

- Paginate a dataset with simple `page` and `page_size` parameters.
- Paginate a dataset with hypermedia metadata.
- Implement pagination that is resilient to deletions within the dataset.

## Requirements

- **Python Version**: Python 3.7 will be used to interpret and compile all files.
- **Style Guide**: The code must adhere to the `pycodestyle` style guide (version 2.5.*).
- **Documentation**: All modules and functions must include documentation explaining their purpose and usage.

## Tasks

### Task 0: Simple Helper Function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
- Page numbers are 1-indexed.

**File:** `0-simple_helper_function.py`

Example usage:

```python
index_range(1, 7)  # Returns: (0, 7)
index_range(3, 15)  # Returns: (30, 45)
```

### Task 1: Simple Pagination
### Task 2: Hypermedia Pagination
### Task 3: Deletion-Resilient Hypermedia Pagination

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/holbertonschool-web_back_end
cd pagination
```

2. Run the Python files:
```bash
git clone https://github.com/holbertonschool-web_back_end
cd pagination
```

## Code Style
Ensure your code follows the pycodestyle style guide:
```bash
pycodestyle your_file.py
```

## Documentation
Verify that all your modules and functions have proper documentation:
```bash
python3 -c 'print(__import__("your_module").__doc__)'
python3 -c 'print(__import__("your_module").your_function.__doc__)'
```
