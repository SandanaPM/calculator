import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calculator import CalculationError, ScientificCalculator, ValidationError
from history import HistoryManager


class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ScientificCalculator()

    def test_divide(self):
        self.assertEqual(self.calculator.calculate("DIVIDE", ["25", "5"]), 5.0)

    def test_square_root(self):
        self.assertEqual(self.calculator.calculate("SQRT", ["144"]), 12.0)

    def test_sine_90_degrees(self):
        self.assertEqual(self.calculator.calculate("SIN", ["90"]), 1.0)

    def test_division_by_zero(self):
        with self.assertRaises(CalculationError):
            self.calculator.calculate("DIVIDE", ["10", "0"])

    def test_invalid_number(self):
        with self.assertRaises(ValidationError):
            self.calculator.calculate("ADD", ["ten", "5"])

    def test_negative_square_root(self):
        with self.assertRaises(CalculationError):
            self.calculator.calculate("SQRT", ["-4"])

    def test_factorial(self):
        self.assertEqual(self.calculator.calculate("FACTORIAL", ["5"]), 120.0)

    def test_log10(self):
        self.assertEqual(self.calculator.calculate("LOG10", ["100"]), 2.0)


class TestHistoryManager(unittest.TestCase):
    def test_history_persistence(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "history.json"
            history = HistoryManager(str(path))
            history.add("DIVIDE", ["25", "5"], "5.0")

            new_history = HistoryManager(str(path))
            self.assertEqual(len(new_history.records), 1)
            self.assertEqual(new_history.records[0]["result"], "5.0")

    def test_history_search_and_sort(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "history.json"
            history = HistoryManager(str(path))
            history.add("ADD", ["2", "3"], "5.0")
            history.add("DIVIDE", ["25", "5"], "5.0")

            self.assertEqual(len(history.search("divide")), 1)
            self.assertEqual(history.sort_records("operation")[0]["operation"], "DIVIDE")


if __name__ == "__main__":
    unittest.main()
