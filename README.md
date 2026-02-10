Python Module 06 — The Codex 🧪
Mastering Python Imports & Packages

This repository is part of a personal Python learning journey focused on clarity, mental models, and explainable code, with special emphasis on code organization and import architecture.

The goal of this module is to understand how Python modules and packages work in real projects, and how developers can control what a package exposes through __init__.py, while avoiding common architectural pitfalls such as circular dependencies.

This module is about structure and intent, not syntax.

🎯 Objectives

By completing this module, the learner is able to:

Understand the difference between modules and packages

Learn the role of __init__.py as a package interface

Control the public API of a package

Practice different import styles and their trade-offs

Compare absolute vs relative imports

Avoid circular dependencies using safe and explicit techniques

Write code that is easy to read, test, and defend

🧠 Topics Covered

Python modules vs packages

The role of __init__.py

Module-level vs package-level access

Explicit exposure of functions

Import styles:

import module

from module import name

import module as alias

Absolute vs relative imports

Circular dependencies and late imports

Clean repository structure for scalable projects

🧪 Exercises Overview
Part I — The Sacred Scroll

Focus: Package initialization and public API control

Create a real Python package

Define internal modules

Expose selected functions through __init__.py

Demonstrate controlled access at package level

Part II — Import Transmutation

Focus: Understanding different import styles

Import full modules vs specific functions

Use of aliases for readability

Multiple imports from the same module

Observe namespace clarity and coupling trade-offs

Part III — The Great Pathway Debate

Focus: Absolute vs relative imports

Use absolute imports from subpackages

Use relative imports within a package

Compare clarity vs conciseness

Expose subpackage functionality via __init__.py

Part IV — Breaking the Circular Curse

Focus: Avoiding circular dependencies

Understand what circular dependencies are and why they are dangerous

Apply late imports to break dependency cycles

Demonstrate valid and invalid execution paths without crashes

🧩 Design Principles

Explicit is better than implicit

Packages should expose only what is intended

Imports are part of the architecture, not an afterthought

Prefer clarity over cleverness

One responsibility per module

Code must be easy to explain during review or evaluation

🛠️ Technical Constraints

Python 3.10+

flake8 compliant

Standard library only

Clear separation between logic and execution

No manipulation of sys.path

Functions kept intentionally simple to focus on imports

# noqa: F401 used intentionally in __init__.py files to define public APIs

📌 Notes

This module is not about complex logic.

It focuses on understanding how Python loads code, how imports behave in real projects, and how developers design clean, maintainable package interfaces.

Being able to explain why a function is accessible or not is as important as making the code run.

