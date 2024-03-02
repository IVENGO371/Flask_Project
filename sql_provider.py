import os
from string import Template


class SQLProvider:
    def __init__(self, file_path: str):
        self._script = {}

        for file in os.listdir(file_path):
            sql = open(f'{file_path}/{file}', encoding='utf-8').read()
            self._script[file] = Template(sql)

    def get(self, prod_name, **kwargs):
        sql = self._script[prod_name].substitute(**kwargs)

        return sql
