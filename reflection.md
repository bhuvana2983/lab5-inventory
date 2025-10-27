\### Reflection — Static Code Analysis Lab



1\. Which issues were easiest and hardest to fix?

The easiest was changing mutable default arguments.  

The hardest was deciding which exceptions to catch without hiding real bugs.



2\. Any false positives? 

Pylint suggested minor style issues that did not affect functionality.



3\. How would you integrate these tools into real workflow?

Use pre-commit hooks locally and GitHub Actions for automatic linting in CI.



4\. Improvements observed:

Code now closes files properly, uses safe logging, validates input, and avoids security risks like `eval()`.  

It’s cleaner, more readable, and more reliable.



