import math
from typing import Callable, Dict, List, Tuple


class CalculatorError(Exception):
    """Base exception for calculator-related errors."""


class ValidationError(CalculatorError):
    """Raised when user input is invalid."""


class CalculationError(CalculatorError):
    """Raised when a mathematical operation cannot be completed."""


class ScientificCalculator:
    """Performs arithmetic and scientific calculations."""

    def __init__(self) -> None:
        self.operations: Dict[str, Callable[..., float]] = {
            "ADD": self.add,
            "SUBTRACT": self.subtract,
            "MULTIPLY": self.multiply,
            "DIVIDE": self.divide,
            "MODULO": self.modulo,
            "POWER": self.power,
            "SQRT": self.sqrt,
            "FACTORIAL": self.factorial,
            "SIN": self.sin,
            "COS": self.cos,
            "TAN": self.tan,
            "LOG10": self.log10,
            "LN": self.ln,
        }

    @staticmethod
    def _require_number(value: str) -> float:
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"'{value}' is not a valid number.") from exc

    @staticmethod
    def _require_count(operation: str, operands: List[str], expected: int) -> None:
        if len(operands) != expected:
            word = "operand" if expected == 1 else "operands"
            raise ValidationError(
                f"{operation} requires exactly {expected} {word}."
            )

    @staticmethod
    def _clean_result(value: float) -> float:
        """Remove insignificant floating-point noise around zero."""
        if abs(value) < 1e-12:
            return 0.0
        return value

    def calculate(self, operation: str, operands: List[str]) -> float:
        operation = operation.strip().upper()

        if operation not in self.operations:
            raise ValidationError(
                f"Unknown operation '{operation}'. "
                f"Use: {', '.join(self.operations.keys())}."
            )

        try:
            return self.operations[operation](*operands)
        except TypeError as exc:
            # This is converted into a clearer validation error for malformed input.
            raise ValidationError(str(exc)) from exc

    def add(self, a: str, b: str) -> float:
        return self._require_number(a) + self._require_number(b)

    def subtract(self, a: str, b: str) -> float:
        return self._require_number(a) - self._require_number(b)

    def multiply(self, a: str, b: str) -> float:
        return self._require_number(a) * self._require_number(b)

    def divide(self, a: str, b: str) -> float:
        numerator = self._require_number(a)
        denominator = self._require_number(b)
        if denominator == 0:
            raise CalculationError("Division by zero is not allowed.")
        return numerator / denominator

    def modulo(self, a: str, b: str) -> float:
        numerator = self._require_number(a)
        denominator = self._require_number(b)
        if denominator == 0:
            raise CalculationError("Modulo by zero is not allowed.")
        return numerator % denominator

    def power(self, a: str, b: str) -> float:
        base = self._require_number(a)
        exponent = self._require_number(b)
        try:
            return self._clean_result(base ** exponent)
        except (OverflowError, ValueError) as exc:
            raise CalculationError(f"Power operation failed: {exc}") from exc

    def sqrt(self, a: str) -> float:
        value = self._require_number(a)
        if value < 0:
            raise CalculationError("Square root of a negative number is not real.")
        return math.sqrt(value)

    def factorial(self, a: str) -> float:
        value = self._require_number(a)
        if not value.is_integer() or value < 0:
            raise CalculationError(
                "Factorial requires a non-negative integer."
            )
        if value > 170:
            raise CalculationError("Factorial is limited to 170 to avoid overflow.")
        return float(math.factorial(int(value)))

    def sin(self, a: str) -> float:
        degrees = self._require_number(a)
        return self._clean_result(math.sin(math.radians(degrees)))

    def cos(self, a: str) -> float:
        degrees = self._require_number(a)
        return self._clean_result(math.cos(math.radians(degrees)))

    def tan(self, a: str) -> float:
        degrees = self._require_number(a)
        # tan(90 + 180k) is undefined.
        normalized = (degrees - 90) / 180
        if math.isclose(normalized, round(normalized), abs_tol=1e-12):
            raise CalculationError("Tangent is undefined at this angle.")
        return self._clean_result(math.tan(math.radians(degrees)))

    def log10(self, a: str) -> float:
        value = self._require_number(a)
        if value <= 0:
            raise CalculationError("LOG10 requires a positive number.")
        return math.log10(value)

    def ln(self, a: str) -> float:
        value = self._require_number(a)
        if value <= 0:
            raise CalculationError("LN requires a positive number.")
        return math.log(value)


def format_result(value: float) -> str:
    """Return a readable result while preserving decimal accuracy."""
    if math.isfinite(value) and value.is_integer():
        return f"{value:.1f}"
    return f"{value:.10g}"
