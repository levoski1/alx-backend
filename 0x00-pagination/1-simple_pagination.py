#!/usr/bin/env python3
"""
Module to provide a server class for paginating a dataset of popular baby names.
"""

import csv
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    The class reads from a CSV file and provides paginated access to the data.
    """
    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        Initialize the Server instance.
        """
        self.__dataset: List[List[str]] = []

    def dataset(self) -> List[List[str]]:
        """
        Return the dataset from the CSV file, loading it if necessary.
        
        The dataset is cached after the first load for efficient access.
        
        Returns:
            List[List[str]]: The dataset excluding the header row.
        """
        if not self.__dataset:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a page of the dataset.
        
        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items per page.
        
        Returns:
            List[List[str]]: A list of rows for the specified page.
        
        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Calculate start and end indexes for the requested page
        start_index, end_index = index_range(page, page_size)

        # Fetch and return the appropriate slice of the dataset
        dataset = self.dataset()
        return dataset[start_index:end_index]
