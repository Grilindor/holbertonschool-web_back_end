#!/usr/bin/env python3
"""
Simple pagination module.

This module contains a Server class that allows pagination
of a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    :param page: The page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple containing the start index and end index for the page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.

    The class reads from a CSV file and caches the dataset after the first load
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset, loading it from the CSV file if necessary.

        :return: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Cache the dataset, skipping the header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.

        :param page: The page number (1-indexed).
        :param page_size: The number of items per page.
        :return: A list of rows representing the page of data.
        """
        # Ensure that the page and page_size are valid integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end index for the requested page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # If the start index is out of range, return an empty list
        if start_index >= len(dataset):
            return []

        # Return the appropriate slice of the dataset
        return dataset[start_index:end_index]
