#!/usr/bin/env python3
""" 1. Simple pagination """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    param page: begin at page 1
    param page_size: number of element in one page

    return a Tuple with start_index, end_index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ take 2 arguments """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retourne un dictionnaire contenant des informations sur
        la page de données."""
        data = self.get_page(page, page_size)

        # Utilise la méthode get_page pour obtenir données de la page actuelle
        data = self.get_page(page, page_size)

        # Calcule le nombre total d'éléments dans le dataset
        total_items = len(self.dataset())

        # Calcule le nombre total de pages
        total_pages = math.ceil(total_items / page_size)

        # Détermine le numéro de la page suivante
        next_page = page + 1 if page * page_size < total_items else None

        # Détermine le numéro de la page précédente
        prev_page = page - 1 if page > 1 else None

    # Construire le dictionnaire de réponse avec les informations de pagination
        return {
            'page_size': len(data),  # Nombre d'éléments sur la page actuelle
            'page': page,            # Numéro de la page actuelle
            'data': data,            # Données de la page actuelle
            'next_page': next_page,  # Num page suiv ou None if no nex page
            'prev_page': prev_page,  # Num page précé or if no de page précé
            'total_pages': total_pages  # Nombre total de pages dans le dataset
        }
