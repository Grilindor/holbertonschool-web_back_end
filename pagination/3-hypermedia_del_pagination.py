#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a page of data, resilient to item deletions.
        :param index: Starting index for the page
        :param page_size: Number of items per page
        :return: Dictionary containing paginated data and additional
        information
        """
        index = 0 if index is None else index
        dataset = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(dataset)
        assert isinstance(page_size, int) and page_size > 0
        index_data = self.indexed_dataset()
        data = []
        current_index = index
        count_items = 0
        while count_items < page_size and current_index < len(index_data):
            if current_index in index_data:
                data.append(index_data[current_index])
                items_count += 1
            current_index += 1

        next_index = current_index if current_index < len(index_data) else None
        return {
             'index': index,
             'next_index': next_index,
             'page_size': len(data),
             'data': data
            }
