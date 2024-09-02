#!/usr/bin/env python3
"""
This module provides a function to calculate the start and end indexes
for paginated data.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for items on a specific page
    given the page number and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and the end index (exclusive) for the items on the specified page.
    """
    first_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return first_index, end_index

