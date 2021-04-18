from dataclasses import dataclass 
from typing import List

@dataclass(frozen=True)
class Column:
    name: str
    dtype: str

@dataclass(frozen=True)
class Table:
    name: str 
    columns: List[Column]
    size: float
    nrows: int 

    @property 
    def size_gb(self):
        return self.size / 1024 / 1024 / 1024

@dataclass(frozen=True)
class Schema:
    name: str 
    tables: List[Table]

@dataclass(frozen=True)
class DataWarehouse:
    name: str 
    schemas: List[Schema]
    region: str


