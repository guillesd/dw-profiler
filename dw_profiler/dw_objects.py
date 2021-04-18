from dataclasses import dataclass 

@dataclass(frozen=True)
class Column:
    name: str
    dtype: str

@dataclass(frozen=True)
class Table:
    name: str 
    columns: list[Column]
    size: float 
    nrows: int 

@dataclass(frozen=True)
class Schema:
    name: str 
    tables: list[Table]

@dataclass(frozen=True)
class DataWarehouse:
    name: str 
    schemas: list[Schema]