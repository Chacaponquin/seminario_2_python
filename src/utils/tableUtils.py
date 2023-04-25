from rich.table import Table
from rich.console import Console


def define_table():
    return Table(border_style="green")


def define_table_column(table: Table, column_name: str):
    table.add_column(column_name, style="green", no_wrap=True)


def print_table(table: Table):
    console = Console()
    console.print(table)