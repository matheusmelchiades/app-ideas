import csv
from pathlib import Path
import functools

ROOT_DIR = Path(__file__).parent.parent
DATA_PATH = f'{ROOT_DIR}/data/planets_2020.04.10_06.49.44.csv'


class Core:

    def __init__(self):
        """
            When instace the Database, start the process of read file data and map all columns
        """
        self.data = []
        self.columnMap = {}

        with open(DATA_PATH, 'r', newline='') as file:
            for row in file:
                if not '#' in row and row:
                    row = row.replace('\n', '')
                    self.data.append(row.split(','))

            for index, value in enumerate(self.data[0]):
                self.columnMap[index] = value

            self.data = self.data[1:]
        pass

    def factory_response(self, data):
        response = []

        for row in data:
            item = {}

            for index, value in enumerate(row):
                field = self.columnMap[index]
                item[field] = value

            response.append(item)

        return response


class Database(Core):

    def __init__(self):
        super().__init__()

    def find(self):

        return super().factory_response(self.data)
