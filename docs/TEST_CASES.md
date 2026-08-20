# Smart Scientific Calculator — Test Cases

| ID | Test Input | Expected Result | Type | Status |
|---|---|---|---|---|
| TC01 | `DIVIDE 25 5` | `5.0` | Normal | Pass |
| TC02 | `SQRT 144` | `12.0` | Normal scientific | Pass |
| TC03 | `SIN 90` | `1.0` | Boundary/scientific | Pass |
| TC04 | `DIVIDE 10 0` | Error: division by zero is not allowed | Invalid | Pass |
| TC05 | `ADD ten 5` | Error: invalid number | Invalid | Pass |
| TC06 | `SQRT -4` | Error: negative square root is not real | Invalid/domain | Pass |
| TC07 | `FACTORIAL 5` | `120.0` | Normal | Pass |
| TC08 | `LOG10 100` | `2.0` | Normal scientific | Pass |
| TC09 | Run a calculation, close program, reopen and select View History | Previous calculation remains available | Persistence | Pass |
| TC10 | Search history for `DIVIDE` | Only matching DIVIDE records are displayed | Search/filter | Pass |
| TC11 | Sort history by `operation` ASC | Records appear alphabetically by operation | Sorting | Pass |
| TC12 | `MODULO 10 0` | Error: modulo by zero is not allowed | Invalid | Pass |

## Automated Test Command

```powershell
python -m unittest discover -s tests -v
```

## Manual Demonstration Scenarios

1. Start the application and show the main menu.
2. Execute `DIVIDE 25 5`.
3. Execute a scientific operation such as `SIN 90`.
4. Attempt `DIVIDE 10 0` and show the error message.
5. Open history and show saved results.
6. Search history for `DIVIDE`.
7. Sort history by operation.
8. Exit and restart the application to demonstrate JSON persistence.
