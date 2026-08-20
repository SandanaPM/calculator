# Project Report — Smart Scientific Calculator

## 1. Problem Understanding

The selected problem is to build a reliable menu-driven calculator that performs arithmetic and scientific operations while handling invalid input and preserving calculation history.

A useful calculator should not only calculate a result; it should also provide clear errors, allow previous calculations to be reviewed, and retain history after the application is closed.

## 2. Proposed Approach

The solution is divided into three main modules:

- `calculator.py` — mathematical operations, validation, and calculation errors.
- `history.py` — JSON-based history persistence, search, and sorting.
- `main.py` — user interface, menu handling, command parsing, and application flow.

This separation keeps the code maintainable and makes individual components easier to test.

## 3. Implementation

### Calculator Module

A `ScientificCalculator` class contains the supported operations. A dictionary maps operation names to methods, allowing the application to validate and dispatch commands cleanly.

Supported operations:

- ADD
- SUBTRACT
- MULTIPLY
- DIVIDE
- MODULO
- POWER
- SQRT
- FACTORIAL
- SIN
- COS
- TAN
- LOG10
- LN

### Validation and Exception Handling

The application validates numeric operands and checks mathematical constraints such as:

- Division by zero
- Modulo by zero
- Square root of a negative number
- Logarithm of zero or a negative number
- Factorial of a negative or non-integer number
- Undefined tangent angles
- Incorrect operand counts
- Unknown operations

Custom exceptions make errors easier to understand and handle.

### History and Persistence

Each successful calculation is stored as a dictionary containing:

- Timestamp
- Operation
- Operands
- Result

Records are saved to `data/history.json`. JSON was selected because it is lightweight, human-readable, and included in Python's standard library.

### Search and Sorting

History can be searched using a keyword that matches operations, operands, or results. Records can also be sorted by timestamp, operation, or result.

## 4. Important Technical Decisions

### Standard Library Only

The application uses only Python's standard library. This keeps the project zero-cost, portable, and easy to install.

### Object-Oriented Design

The `ScientificCalculator` and `HistoryManager` classes group related responsibilities and demonstrate appropriate use of OOP.

### JSON Persistence

JSON is sufficient for a small local application and avoids the complexity of a database.

### Command Support

In addition to the numbered menu, direct commands such as `DIVIDE 25 5` are accepted. This directly supports the specified sample input format.

## 5. Testing Performed

Automated tests were written using `unittest`.

The tests cover:

- Normal arithmetic
- Scientific operations
- Boundary values
- Invalid numeric input
- Division by zero
- Invalid square roots
- Factorial
- Logarithms
- JSON persistence
- History search
- History sorting

Manual testing was also planned for the major user-interface flows.

## 6. Challenges Encountered

### Challenge 1: Invalid Input

Users may enter letters instead of numbers or an incorrect number of operands.

**Solution:** Numeric conversion and operand-count validation are performed before calculations.

### Challenge 2: Mathematical Errors

Operations such as division, logarithms, square roots, and tangent have mathematical restrictions.

**Solution:** Explicit domain checks raise clear `CalculationError` messages.

### Challenge 3: Data Persistence

History must survive application restarts.

**Solution:** Successful calculations are written to a JSON file and loaded when the application starts.

### Challenge 4: Maintainability

Putting all functionality in one file would make testing and future changes difficult.

**Solution:** Responsibilities are separated into calculator, history, and UI modules.

## 7. Future Scope

- Tkinter graphical user interface
- Expression parser
- Degree/radian switch
- CSV export
- Calculator memory functions
- Statistical functions
- Custom precision settings
- Additional automated tests
- Accessibility improvements

## 8. Conclusion

The Smart Scientific Calculator meets the core requirements of a functional Python application while demonstrating foundational programming concepts. It combines modular programming, OOP, validation, exception handling, file handling, JSON persistence, search, sorting, and testing in a practical project.

The project is intentionally simple enough to understand and explain while still providing features beyond basic arithmetic.
