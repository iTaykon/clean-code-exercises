# This code allows you to store information on people owing you money
# and then list all those people in a ordered and formatted way in the terminal.
# Try to improve the `payday` function by splitting the logic into smaller functions.

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Debtor:
    """Stores the information on a person owing us money"""
    name: str
    debt: float

    def print_debtor_info(self):
        if self._has_high_debt():
            print(f"{self.name}: !!!{self.debt}!!!")
        else:
            print(f"{self.name}: {self.debt}")

    def _has_high_debt(self):
        return self.debt > 100.0


def payday(debtors: Iterable[Debtor]) -> None:
    sorted_debtors = sort_debtors(debtors)

    for debtor in sorted_debtors:
        debtor.print_debtor_info()
    

def sort_debtors(debtors: Iterable[Debtor]):
    return reversed(sorted(debtors, key=lambda debtor: debtor.debt))


if __name__ == "__main__":
    payday([
        Debtor("Person1", 100.0),
        Debtor("Person2", 200.0),
        Debtor("Person3", 10.0),
        Debtor("Person4", 50.0),
        Debtor("Person5", 1250.0)
    ])
