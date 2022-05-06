"""This is a sample template."""
from __future__ import annotations


def function(name: str) -> None:
    """Printing name."""
    print(f"my name is {name}")


def main():
    """Calling function."""
    name = input()
    function(name)


if __name__ == "__main__":
    main()
