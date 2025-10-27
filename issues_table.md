| Issue Type | Tool | Line(s) | Description | Fix Approach |

|-------------|------|---------|--------------|---------------|

| Missing module docstring | Pylint | 1 | No top-level description of the module | Add a brief docstring at the top explaining the script purpose |

| Non-snake\_case function names | Pylint | 16, 31, 50, 55, 69, 79, 86 | Functions use CamelCase (addItem, removeItem, etc.) | Rename to snake\_case (e.g., add\_item, remove\_item) for PEP8 compliance |

| Catching too general exception | Pylint | 46, 75 | Broad `except Exception` used | Replace with specific exceptions (e.g., `except FileNotFoundError`, `except KeyError`) |

| Use of global statement | Pylint | 57 | `global stock\_data` used inside function | Pass stock\_data as an argument or manage within a class |

| Logging string interpolation | Pylint | 23–47 | Using f-strings inside logging methods | Use lazy logging: `logging.info("Added %s of %s", qty, item)` instead of f-string |

| Missing function/method docstrings | Pylint | 91 (and other functions) | Functions have no documentation strings | Add docstrings to describe purpose and parameters |

| Line too long (83 > 79 chars) | Flake8 | 43 | One line exceeds recommended length | Split long line or use implicit line continuation |

| Security issues | Bandit | — | No issues identified | No action needed |



