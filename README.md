# Smart Scientific Calculator

## 1. Problem Statement

Basic calculators often provide only immediate arithmetic results and do not provide a structured way to validate input, review previous calculations, search history, or preserve data between program runs.

The **Smart Scientific Calculator** solves this problem with a menu-driven Python application that supports arithmetic and scientific operations, strong validation, exception handling, searchable/sortable history, and JSON-based persistence.

## 2. Objective

To develop a clean, reliable, zero-cost Python calculator that demonstrates foundational programming concepts while providing useful scientific-calculator functionality.

## 3. Features

- Menu-driven command-line interface
- Direct command support such as `DIVIDE 25 5`
- Arithmetic operations: ADD, SUBTRACT, MULTIPLY, DIVIDE, MODULO, POWER
- Scientific operations: SQRT, FACTORIAL, SIN, COS, TAN, LOG10, LN
- Trigonometric calculations in degrees
- Input validation
- Exception handling
- Division/modulo by zero protection
- Mathematical-domain validation
- Persistent calculation history in JSON
- History search/filter
- History sorting by timestamp, operation, or result
- Clear-history option with confirmation
- Unit tests using Python's built-in `unittest`
- Standard-library-only implementation

## 4. Technologies Used

- Python 3.9+
- `math`
- `json`
- `datetime`
- `pathlib`
- `shlex`
- `unittest`

No paid API, database server, framework, or external package is required.

## 5. Installation / Setup

### Windows

1. Install Python 3.9 or later.
2. Open PowerShell in the project folder.
3. Verify Python:

```powershell
python --version
```

4. No external packages are required.

### Linux / macOS

```bash
python3 --version
```

No external installation is required.

## 6. How to Run

From the project root:

### Windows

```powershell
python src/main.py
```

### Linux / macOS

```bash
python3 src/main.py
```

The program creates `data/history.json` automatically after the first successful calculation.

## 7. Example

Direct command:

```text
Enter your choice or a direct command: DIVIDE 25 5
Result: 5.0
History: saved successfully.
```

Menu mode:

```text
Enter your choice or a direct command: 9
Enter 1 operand(s) for SIN, separated by spaces: 90
Result: 1.0
History: saved successfully.
```

## 8. Project Structure

```text
Smart_Scientific_Calculator/
│
├── src/
│   ├── calculator.py
│   ├── history.py
│   └── main.py
│
├── tests/
│   └── test_calculator.py
│
├── data/
│   └── history.json              # created automatically
│
├── docs/
│   ├── TEST_CASES.md
│   └── PROJECT_REPORT.md
│
├── screenshots/
│   └── README.txt
│
└── README.md
```

## 9. Testing

Run all automated tests from the project root:

```powershell
python -m unittest discover -s tests -v
```

The test suite covers arithmetic, scientific calculations, invalid input, division by zero, negative square root, factorial, logarithms, persistence, search, and sorting.

## 10. Limitations

- The interface is command-line based.
- Trigonometric functions currently use degrees only.
- Complex-number calculations are not supported.
- History is stored locally in a JSON file and is not encrypted.
- Very large factorial values are limited to prevent floating-point overflow.

## 11. Future Improvements

- Add a graphical interface using Tkinter.
- Add radian/degree switching.
- Add expression parsing such as `(25 + 5) * 2`.
- Add memory functions such as M+, M-, MR, and MC.
- Export history to CSV.
- Add configurable decimal precision.
- Add themes and accessibility improvements.
- Add a statistics module for mean, median, and standard deviation.

## 12. Development Process

The project followed:

**Understand → Analyse → Design → Implement → Test → Document**

The application was designed first around operation requirements, validation rules, history behaviour, and persistence before implementation.

## 13. AI Usage

AI tools may be used as learning and development assistance for understanding concepts, debugging, researching documentation, or reviewing implementation. The submitted implementation should be understood by the student and explained during evaluation.

## 14. Evaluation Readiness

The project demonstrates:

- Functions and modular programming
- Lists and dictionaries
- Conditional logic and loops
- Input validation
- Exception handling
- File handling and JSON
- Object-oriented programming
- Search, filtering, and sorting
- Data persistence
- Testing and documentation
- Clean project organization
