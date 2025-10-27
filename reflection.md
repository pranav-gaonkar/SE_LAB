# Lab 5: Static Code Analysis Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issue to fix was the **Insecure Function (eval())**. This was solved simply by deleting or commenting out the single line of code.

The hardest issue was the **Non-PEP 8 Naming (C0103)**. Although the fix was straightforward (renaming functions to `snake_case`), it was tedious because I had to check and update every single call to those functions throughout the `main()` block and other parts of the script to prevent runtime errors.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

One potential false positive reported was the **Unused Import (`import logging`)**. While the tool correctly identified that the module wasn't used in the provided code, it might have been left there intentionally by a developer planning to implement logging later. The tool flags it as unnecessary clutter, but a developer might view it as temporary work-in-progress.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate static analysis tools in two main ways:

* **Local Development (Pre-commit Hooks):** I would set up the tools (Pylint, Bandit, Flake8) to run automatically whenever a developer tries to commit code locally. This acts as a quality gate, preventing code with simple style errors (Flake8) or critical bugs (Pylint) from even being added to the repository.
* **Continuous Integration (CI):** I would integrate the tools into a CI/CD pipeline (like GitHub Actions). The pipeline would run Bandit for security checks on every pull request. If the code introduces any high or medium security vulnerabilities, the pipeline would fail, blocking the code from being merged into the main branch.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

* **Robustness:** Fixing the **Bare `except`** and the **Mutable Default Argument** significantly improved robustness by ensuring the code handles errors specifically (`KeyError`) instead of silently ignoring all failures, and prevented subtle, hard-to-debug bugs related to shared list state.
* **Readability:** Renaming all functions to **snake\_case** dramatically improved readability and adherence to Python standards (PEP 8), making the code easier for any new developer to understand.
* **Security:** Removing the **`eval()`** call immediately eliminated a major, critical security vulnerability.