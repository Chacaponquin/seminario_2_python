from rich.table import Table
from rich.console import Console


def define_table():
    return Table(border_style="green")


def define_table_column(table: Table, columnName: str):
    table.add_column(columnName, style="green", no_wrap=True)


def print_table(self, table: Table):
    console = Console()
    console.print(table)