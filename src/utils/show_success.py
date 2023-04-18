from rich import print as rprint


def show_success(message: str) -> None:
    rprint(f'[bold blue]{message}')