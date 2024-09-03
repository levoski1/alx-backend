# Pagination and Deletion-Resilient Hypermedia Pagination

This repository contains Python scripts that demonstrate pagination, hypermedia pagination, and deletion-resilient pagination techniques using a dataset of popular baby names.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Simple Helper Function](#task-0-simple-helper-function)
  - [Task 1: Server Pagination](#task-1-server-pagination)
  - [Task 2: Deletion-Resilient Hypermedia Pagination](#task-2-deletion-resilient-hypermedia-pagination)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Introduction

The aim of this project is to implement pagination and hypermedia pagination techniques in Python. The scripts allow for efficient data retrieval from a dataset of popular baby names, including handling cases where data might be deleted while maintaining consistent pagination results.

## Project Structure

The project is organized into the following files:

- `0-simple_helper_function.py`: A helper function to compute the index range for pagination.
- `1-server.py`: A script that defines a `Server` class to paginate a dataset using the helper function.
- `2-hypermedia_pagination.py`: A script that defines a `Server` class to perform deletion-resilient hypermedia pagination.
- `Popular_Baby_Names.csv`: A sample dataset containing popular baby names.
- `README.md`: This file, which provides an overview of the project and usage instructions.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Pycodestyle (version 2.5.\*)
- `wc` utility for checking file lengths

All files must:
- Have a shebang line `#!/usr/bin/env python3`.
- End with a new line.
- Follow the pycodestyle style guide.
- Include proper documentation for modules, classes, and methods.

## Tasks

### Task 0: Simple Helper Function

File: `0-simple_helper_function.py`

- **Objective**: Create a helper function `index_range` that takes two integer arguments, `page` and `page_size`, and returns a tuple containing the start and end indexes for pagination.
- **Requirements**: The function should be type-annotated, properly documented, and follow the pycodestyle guide.

### Task 1: Server Pagination

File: `1-server.py`

- **Objective**: Implement a `Server` class that reads a dataset from a CSV file and provides paginated access to the data using the `index_range` helper function.
- **Methods**:
  - `dataset()`: Loads and caches the dataset.
  - `get_page(page: int, page_size: int)`: Returns a specific page of data.
- **Requirements**: The class and its methods should be type-annotated, properly documented, and follow the pycodestyle guide.

### Task 2: Deletion-Resilient Hypermedia Pagination

File: `2-hypermedia_pagination.py`

- **Objective**: Extend the `Server` class to support deletion-resilient hypermedia pagination.
- **Methods**:
  - `indexed_dataset()`: Returns a dataset indexed by its position.
  - `get_hyper_index(index: int, page_size: int)`: Returns a page of data while accounting for potential deletions.
- **Requirements**: The class and its methods should be type-annotated, properly documented, and follow the pycodestyle guide.

## Usage

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Run the Scripts**:

- To run the helper function script:
    ```sh
    python3 0-simple_helper_function.py
    ```

- To run the server pagination script:
    ```sh
    python3 1-server.py
    ```

- To run the deletion-resilient hypermedia pagination script:
    ```sh
    python3 2-hypermedia_pagination.py
    ```

3. **Test**:
    Use the provided test cases in each file or write your own tests to verify the functionality.

## Testing

- Ensure all files adhere to the pycodestyle guide:
    ```sh
    pycodestyle <filename>
    ```
- Test file lengths using the `wc` utility:
    ```sh
    wc -l <filename>
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
