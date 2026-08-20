import shlex
from pathlib import Path
from typing import List, Optional, Tuple

from calculator import (
    CalculationError,
    ScientificCalculator,
    ValidationError,
    format_result,
)
from history import HistoryManager


APP_TITLE = "Smart Scientific Calculator"
BASE_DIR = Path(__file__).resolve().parent.parent
HISTORY_FILE = BASE_DIR / "data" / "history.json"


MENU_OPERATIONS = {
    "1": "ADD",
    "2": "SUBTRACT",
    "3": "MULTIPLY",
    "4": "DIVIDE",
    "5": "MODULO",
    "6": "POWER",
    "7": "SQRT",
    "8": "FACTORIAL",
    "9": "SIN",
    "10": "COS",
    "11": "TAN",
    "12": "LOG10",
    "13": "LN",
}


def print_header() -> None:
    print("\n" + "=" * 68)
    print(f"{APP_TITLE:^68}")
    print("=" * 68)


def print_menu() -> None:
    print(
        """
1.  ADD        (2 operands)
2.  SUBTRACT   (2 operands)
3.  MULTIPLY   (2 operands)
4.  DIVIDE     (2 operands)
5.  MODULO     (2 operands)
6.  POWER      (2 operands)
7.  SQRT       (1 operand)
8.  FACTORIAL  (1 operand)
9.  SIN        (degrees, 1 operand)
10. COS        (degrees, 1 operand)
11. TAN        (degrees, 1 operand)
12. LOG10      (1 operand)
13. LN         (1 operand)

14. VIEW HISTORY
15. SEARCH HISTORY
16. SORT HISTORY
17. CLEAR HISTORY
0.  EXIT

Tip: You can also enter commands directly, e.g. DIVIDE 25 5
"""
    )


def parse_command(command: str) -> Tuple[str, List[str]]:
    """Parse an operation and its operands from a command string."""
    try:
        parts = shlex.split(command)
    except ValueError as exc:
        raise ValidationError(f"Invalid command syntax: {exc}") from exc

    if not parts:
        raise ValidationError("Please enter an operation.")

    return parts[0].upper(), parts[1:]


def perform_calculation(
    calculator: ScientificCalculator,
    history: HistoryManager,
    operation: str,
    operands: List[str],
) -> Optional[str]:
    """Calculate, print, and persist a successful result."""
    try:
        result = calculator.calculate(operation, operands)
        formatted = format_result(result)
        history.add(operation, operands, formatted)
        print(f"Result: {formatted}")
        print("History: saved successfully.")
        return formatted
    except (ValidationError, CalculationError) as exc:
        print(f"Error: {exc}")
        return None


def display_history(records: List[dict]) -> None:
    if not records:
        print("No history entries found.")
        return

    print("\n" + "-" * 88)
    print(f"{'#':<4}{'Timestamp':<25}{'Operation':<14}{'Operands':<25}{'Result':<15}")
    print("-" * 88)

    for index, record in enumerate(records, start=1):
        operands = " ".join(str(item) for item in record["operands"])
        print(
            f"{index:<4}"
            f"{record.get('timestamp', ''):<25}"
            f"{record.get('operation', ''):<14}"
            f"{operands:<25}"
            f"{record.get('result', ''):<15}"
        )
    print("-" * 88)


def run_direct_command(
    command: str,
    calculator: ScientificCalculator,
    history: HistoryManager,
) -> None:
    operation, operands = parse_command(command)

    if operation in {"HISTORY", "VIEW_HISTORY"}:
        display_history(history.records)
        return

    if operation == "SEARCH":
        keyword = " ".join(operands)
        display_history(history.search(keyword))
        return

    if operation == "CLEAR_HISTORY":
        history.clear()
        print("History cleared.")
        return

    if operation == "SORT":
        key = operands[0].lower() if operands else "timestamp"
        order = operands[1].lower() if len(operands) > 1 else "desc"
        if order not in {"asc", "desc"}:
            raise ValidationError("Sort order must be ASC or DESC.")
        try:
            records = history.sort_records(key, reverse=(order == "desc"))
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc
        display_history(records)
        return

    perform_calculation(calculator, history, operation, operands)


def menu_calculation(
    choice: str,
    calculator: ScientificCalculator,
    history: HistoryManager,
) -> None:
    operation = MENU_OPERATIONS[choice]
    operand_count = 1 if operation in {
        "SQRT", "FACTORIAL", "SIN", "COS", "TAN", "LOG10", "LN"
    } else 2

    raw = input(
        f"Enter {operand_count} operand(s) for {operation}, separated by spaces: "
    ).strip()

    try:
        _, operands = parse_command(f"{operation} {raw}")
        perform_calculation(calculator, history, operation, operands)
    except ValidationError as exc:
        print(f"Error: {exc}")


def main() -> None:
    calculator = ScientificCalculator()
    history = HistoryManager(str(HISTORY_FILE))

    print_header()
    print("All trigonometric functions use degrees.")
    print("History is automatically saved in data/history.json.")

    while True:
        print_menu()
        choice = input("Enter your choice or a direct command: ").strip()

        if not choice:
            print("Error: Please enter a menu choice or operation.")
            continue

        if choice == "0":
            print("Thank you for using Smart Scientific Calculator.")
            break

        if choice in MENU_OPERATIONS:
            menu_calculation(choice, calculator, history)
            continue

        if choice == "14":
            display_history(history.records)
            continue

        if choice == "15":
            keyword = input("Enter keyword to search: ").strip()
            display_history(history.search(keyword))
            continue

        if choice == "16":
            key = input("Sort by timestamp, operation, or result: ").strip().lower()
            order = input("Order (ASC/DESC): ").strip().lower()
            if order not in {"asc", "desc"}:
                print("Error: Sort order must be ASC or DESC.")
                continue
            try:
                display_history(
                    history.sort_records(key, reverse=(order == "desc"))
                )
            except ValueError as exc:
                print(f"Error: {exc}")
            continue

        if choice == "17":
            confirmation = input("Type YES to clear all history: ").strip().upper()
            if confirmation == "YES":
                history.clear()
                print("History cleared.")
            else:
                print("Clear operation cancelled.")
            continue

        try:
            run_direct_command(choice, calculator, history)
        except ValidationError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
