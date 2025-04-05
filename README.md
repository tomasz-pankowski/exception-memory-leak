# 🧠 Memory Leak Demo

This Python project demonstrates a simple memory leak cause by cyclic references to traceback holding reference to the frame object.
This problem only occurs when `gc` collector is disabled and only reference counting is used for memory management.

## How to run
Memory Leak:
```bash
uv run python memory_leak_test.py --mode leak
```

Without Memory Leak:
```bash
uv run python memory_leak_test.py --mode no-leak 
```
problem only occurs when `gc` is disabled
```bash
uv run python memory_leak_test.py --mode leak --gc-enabled
```
---

## ⚙️ Requirements

- Python **3.8 or newer**
- [`uv`](https://github.com/astral-sh/uv) — fast Python package and virtual environment manager

---

## 📦 Installing dependencies

Use `uv` to install dependencies from the `pyproject.toml` file:

```bash
uv pip install -r pyproject.toml
