#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    
    This class provides methods to read a dataset from a CSV file,
    create an indexed version of the dataset, and perform deletion-resilient
    hypermedia pagination.
    """
    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server instance."""
        self.__dataset: List[List[str]] = []
        self.__indexed_dataset: Dict[int, List[str]] = {}

    def dataset(self) -> List[List[str]]:
        """
        Return the cached dataset from the CSV file, loading it if necessary.
        
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

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """
        Return a dataset indexed by its sorting position, starting at 0.
        
        This dataset is cached for efficient access and is resilient to deletions.
        
        Returns:
            Dict[int, List[str]]: The indexed dataset.
        """
        if not self.__indexed_dataset:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, any]:
        """
        Return a page of the dataset in a deletion-resilient manner.
        
        This method provides pagination while accounting for any deletions that
        might have occurred in the dataset.
        
        Args:
            index (int): The current start index of the page.
            page_size (int): The number of items per page.
        
        Returns:
            Dict[str, any]: A dictionary containing the current index, next index,
            page size, and the data for the requested page.
        
        Raises:
            AssertionError: If the index is not within the range of the dataset.
        """
        # Validate inputs
        assert isinstance(index, int) and index >= 0 and index < len(self.indexed_dataset()), \
            "Index must be a non-negative integer within the dataset range."

        current_index = index
        data = []
        indexed_dataset = self.indexed_dataset()

        # Gather data while accounting for deletions
        while len(data) < page_size and current_index < len(indexed_dataset):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            # Increment current_index regardless of whether the item was found
            current_index += 1

        # Determine the next index after gathering the required page_size data
        next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
