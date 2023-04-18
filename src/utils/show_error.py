from rich import print as rprint


def show_error(message: str) -> None:
    rprint(f'[bold red]{message}')
