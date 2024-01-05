from rich.table import Table
from abc import ABC, abstractmethod


class GreatingTable(ABC):

    @abstractmethod
    def get_table(self):
        pass


class BookTable(GreatingTable):

    def __init__(self, data):
        self.data = data

    def get_table(self):
        table = Table()
        table.add_column("Name", style="bright_magenta")
        table.add_column("Phone", style="magenta")
        table.add_column("Birthday", style="cyan")

        for sh in self.data.values():
            table.add_row(
                f"{sh.name}",
                f"{', '.join(p.get_value for p in sh.phones)}",
                f"{sh.birthdays}",

            )
        return table
